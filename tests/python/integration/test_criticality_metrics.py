import unittest
import rtamt
import os

import numpy as np

# Static variables pointing to the location of the examples specs
AD_MONITORS_SPECS_FOLDER = os.path.join('examples', 'ad_monitors', 'specs')

# Utility methods, those could be probably placed somewhere else
def _expected_robustness_of_tcc_measure(velocity_ego: float, velocity_npc: float, relative_distance_ego_npc: float, same_lane_ego_npc: bool):
    """
    Based on the expected quantitative formulation 
    """
    # TODO This is not refactory safe
    safe_ttc = 3.5
    # TODO: do we use PINF/NINF?
    same_lane_ego_npc_as_float = np.PINF if same_lane_ego_npc else np.NINF
    # TODO Shouldn't be also that "npc_is_reacheable_from_ego - or - npc_in_front_of_ego"?

    # cond = same_lane_ego_npc and velocity_ego > velocity_npc
    cond = min(same_lane_ego_npc_as_float, velocity_ego - velocity_npc) * np.PINF

    # cond -> ((relative_distance_ego_npc / (velocity_ego - velocity_npc)) >= safe_ttc)
    return max( - cond, (relative_distance_ego_npc / (velocity_ego - velocity_npc)) - safe_ttc);

# TODO this can be refactored to accept keys and function to compute the robustness
def _compute_expected_robustness(dataSet: dict):
    """
    (M)apply the function to the dataSet to compute the expected ttc
    """
    expected_robustness = []
    for i in range(0, len(dataSet["time"])):
        time = dataSet["time"][i]
        velocity_ego = dataSet["velocity_ego"][i]
        velocity_npc = dataSet["velocity_npc"][i]
        relative_distance_ego_npc = dataSet["relative_distance_ego_npc"][i]
        same_lane_ego_npc = dataSet["same_lane_ego_npc"][i]

        expected_robustness.append([time, _expected_robustness_of_tcc_measure(velocity_ego, velocity_npc, relative_distance_ego_npc, same_lane_ego_npc)])

    return expected_robustness

# TODO Not sure how to inject fixtures here
def _instantiate_the_runtime_monitor_for(criticality_measure_name: str) -> rtamt.StlDiscreteTimeSpecification:
    """
    Follows the naming convention: <criticality_measure_name>.stl
    Assumes that spec is stored directly inside the folder: AD_MONITORS_SPECS_FOLDER
    """
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.spec = spec.get_spec_from_file(os.path.join(AD_MONITORS_SPECS_FOLDER, f"{criticality_measure_name}.stl"))
    spec.parse()
    return spec

# TODO We need to share the dataSets among the criticality metric
class TestAdCriticalityMetrics(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAdCriticalityMetrics, self).__init__(*args, **kwargs)

    # The vehicles share the road, the npc is ahead and parked, the ego travel faster ()
    NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE = {
            'time': [0.0, 0.1, 0.2, 0.3],
            'velocity_ego': [12.0, 11.999602538695664, 11.998449099520837, 11.993527898984228],
            'velocity_npc': [0.0, 0.0, 0.0, 0.0],
            'relative_distance_ego_npc': [66.4227170936, 65.22273038996738, 64.02282178214598, 62.823166528097175],
            'same_lane_ego_npc': [True, True, True, True]
        }
    
    NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE = {
        'time': [0.0, 0.1, 0.2, 0.3],
        'velocity_ego': [12.0, 11.999602538695664, 11.998449099520837, 11.993527898984228],
        'velocity_npc': [0.0, 0.0, 0.0, 0.0],
        # TODO What do we put here? None? Nan? Inf? -Inf?
        'relative_distance_ego_npc': [np.inf, np.inf, np.inf, np.inf],
        'same_lane_ego_npc': [False, False, False, False]
    }

    # TCC
    def test_ttc_two_vehicles_on_the_same_road(self):
        # INSTANTIATE THE UNIT
        tcc_runtime_monitor = _instantiate_the_runtime_monitor_for("ttc")

        # SET EXPECTATIONS    
        expected_robustness = _compute_expected_robustness(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE)

        # CALL THE RUNTIME MONITOR
        actual_robustness = tcc_runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])

    # TCC
    def test_vehicles_not_in_the_same_line(self):
        # INSTANTIATE THE UNIT
        tcc_runtime_monitor = _instantiate_the_runtime_monitor_for("ttc")

        # SET EXPECTATIONS    
        expected_robustness = _compute_expected_robustness(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE)

        # CALL THE RUNTIME MONITOR
        actual_robustness = tcc_runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])
     
if __name__ == '__main__':
    unittest.main()
