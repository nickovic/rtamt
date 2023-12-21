from operator import index
import unittest
import rtamt
import os
from math import sqrt, pow

import numpy as np

from typing import Callable

# Static variables pointing to the location of the examples specs
AD_MONITORS_SPECS_FOLDER = os.path.join('examples', 'ad_monitors', 'specs')

# Utility methods, those could be probably placed somewhere else
def _expected_robustness_of_ttc_measure(index, **kwargs) -> float:
    velocity_ego = kwargs["velocity_ego"][index]
    velocity_npc = kwargs["velocity_npc"][index]
    relative_distance_ego_npc = kwargs["relative_distance_ego_npc"][index]
    same_lane_ego_npc = kwargs["same_lane_ego_npc"][index]

    # TODO This is not refactory safe
    safe_ttc = 3.5
    # TODO: do we use PINF/NINF?
    same_lane_ego_npc_as_float = np.PINF if same_lane_ego_npc else np.NINF
    # TODO Shouldn't be also that "npc_is_reacheable_from_ego - or - npc_in_front_of_ego"?

    # cond = same_lane_ego_npc and velocity_ego > velocity_npc
    cond = min(same_lane_ego_npc_as_float, velocity_ego - velocity_npc) * np.PINF

    # cond -> ((relative_distance_ego_npc / (velocity_ego - velocity_npc)) >= safe_ttc)
    return max( - cond, (relative_distance_ego_npc / (velocity_ego - velocity_npc)) - safe_ttc);

def _expected_robustness_of_rss_measure(index, **kwargs) -> float:
    # Variables
    # TODO Is longitudinal distance computed w.r.t. the road?
    dist_lon_ego_npc: float = kwargs["dist_lon_ego_npc"][index]
    velocity_ego: float = kwargs["velocity_ego"][index]
    velocity_npc: float = kwargs["velocity_npc"][index]

    # Is behind?: Same lane and sign
    back_ego_npc: bool = kwargs["back_ego_npc"][index]
    back_ego_npc_as_float = np.PINF if back_ego_npc else np.NINF

    # Constants - Not refactory safe!
    tau: float = 0.1
    acc_max: float = 5.0
    break_min: float = 4.0
    break_max: float = 8.0

    # Precondition of the monitor
    # cond = back_ego_npc
    cond = back_ego_npc_as_float

    # Definition of Safe Distance
    safe_dist = velocity_ego * tau + 0.5 * acc_max * pow(tau, 2) + pow(velocity_ego + tau*acc_max, 2) / (2 * break_min) - pow(velocity_npc, 2) / (2 * break_max)

    # Robustness of RSS
    # cond -> (dist_lon_ego_npc >= safe_dist)
    # A => B is the same as (NOT A) OR B
    return max( - cond,  (dist_lon_ego_npc - safe_dist))

def _expected_robustness_of_mttc_measure(index, **kwargs) -> float:
    # Variables
    # TODO Is longitudinal distance computed w.r.t. the road?
    dist_lon_ego_npc: float = kwargs["dist_lon_ego_npc"][index]
    velocity_ego: float = kwargs["velocity_ego"][index]
    velocity_npc: float = kwargs["velocity_npc"][index]
    acceleration_ego: float = kwargs["acceleration_ego"][index]
    acceleration_npc: float = kwargs["acceleration_npc"][index]

    # Is behind?: Same lane and sign
    back_ego_npc: bool = kwargs["back_ego_npc"][index]
    back_ego_npc_as_float = np.PINF if back_ego_npc else np.NINF

    # Constants - Not refactory safe!
    safe_ttc: float = 3.5

    # Preconditions and expressions to build the monitor
    delta_v = abs(velocity_ego - velocity_npc)
    delta_a = abs(acceleration_ego - acceleration_npc)

    t1 = - (delta_v) - sqrt(pow(delta_v, 2) + 2*delta_a*dist_lon_ego_npc)
    t2 = - delta_v + sqrt(pow(delta_v, 2) + 2*delta_a*dist_lon_ego_npc)

    # cond = back_ego_npc and velocity_ego > velocity_npc
    # what's the difference between > and >= when we compute robustness?
    cond = min(back_ego_npc_as_float, velocity_ego - velocity_npc)

    # TODO Refactor translation to boolean
    # cond_1 = delta_a > 0
    cond_1 = np.PINF if delta_a > 0 else np.NINF
    
    # cond_2 = t1 > 0
    cond_2 = np.PINF if t1 > 0 else np.NINF

    # cond_3 = t2 > 0
    cond_3 = np.PINF if t2 > 0 else np.NINF

    # cond_4 = t1 < t2
    cond_4 = np.PINF if t1 < t2 else np.NINF

    # a1 = (cond and not cond_1) -> ((dist_lon_ego_npc / (velocity_ego - velocity_npc)) >= safe_ttc)
    # TODO Is dist_lon_ego_npc the same as relative distance?
    a1 = max ( - min(cond, -cond_1), 
              ((dist_lon_ego_npc / (velocity_ego - velocity_npc)) - safe_ttc)
              )

    # a2 = (cond and cond_1 and cond_2 and cond_3 and not cond_4) -> (t1 >= safe_ttc)
    a2 = max( - min(cond, cond_1, cond_2, cond_3, -cond_4),
             (t1 - safe_ttc))
    
    # a3 = (cond and cond_1 and cond_2 and cond_3 and cond_4) -> (t2 >= safe_ttc)
    a3 = max( - min(cond, cond_1, cond_2, cond_3, cond_4),
             (t2 - safe_ttc))
    
    # a4 = (cond and cond_1 and cond_2 and not cond_3) -> (t1 >= safe_ttc)
    a4 = max( - min(cond, cond_1, cond_2, -cond_3),
             (t1 - safe_ttc))

    # a5 = (cond and cond_1 and not cond_2 and cond_3) -> (t2 >= safe_ttc)
    a5 = max( -min(cond, cond_1, -cond_2, cond_3),
             (t2 - safe_ttc))

    # a1 and a2 and a3 and a4 and a5
    return min(a1, a2, a3, a4, a5)



def _get_expected_criticality_metric(criticality_metric: str) -> Callable:
    if "ttc" == criticality_metric:
        return _expected_robustness_of_ttc_measure
    if "mttc" == criticality_metric:
        return _expected_robustness_of_mttc_measure
    if "rss" == criticality_metric:
        return _expected_robustness_of_rss_measure
    
    raise AssertionError(f"Not a valid criticality metric {criticality_metric}")

# TODO this can be refactored to accept keys and function to compute the robustness
def _compute_expected_robustness_of_criticality_metric(dataSet: dict, criticality_metric: str):
    """
    (M)apply the function to the dataSet to compute the expected ttc
    """

    # TODO assume data is sorted by time!    
    expected_robustness = []
    for i in range(0, len(dataSet["time"])):
        time = dataSet["time"][i]
        expected_robustness.append([time, _get_expected_criticality_metric(criticality_metric)(i, **dataSet)])

    return expected_robustness

# TODO Not sure how to inject fixtures here
def _instantiate_the_runtime_monitor_for(criticality_metric: str): #-> AbstractOfflineOnlineSpecification?
    """
    Follows the naming convention: <criticality_measure_name>.stl
    Assumes that spec is stored directly inside the folder: AD_MONITORS_SPECS_FOLDER
    """
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.spec = spec.get_spec_from_file(os.path.join(AD_MONITORS_SPECS_FOLDER, f"{criticality_metric}.stl"))
    spec.parse()
    return spec

# TODO We need to share the dataSets among the criticality metric
class TestAdCriticalityMetrics(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAdCriticalityMetrics, self).__init__(*args, **kwargs)

    # Is behind?: Same lane and sign
    # back_ego_npc: bool = kwargs["back_ego_npc"][index]
    # The vehicles share the road, the npc is ahead and parked, the ego travel faster ()
    NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE = {
            'time': [0.0, 0.1, 0.2, 0.3],
            'velocity_ego': [12.0, 11.999602538695664, 11.998449099520837, 11.993527898984228],
            'velocity_npc': [0.0, 0.0, 0.0, 0.0],
            # M/S^2 or G?
            'acceleration_ego': [1.0, 1.0, 1.0, 1.0],
            'acceleration_npc': [0.0, 0.0, 0.0, 0.0],

            'relative_distance_ego_npc': [66.4227170936, 65.22273038996738, 64.02282178214598, 62.823166528097175],
            'dist_lon_ego_npc': [66.4227170936, 65.22273038996738, 64.02282178214598, 62.823166528097175],
            'same_lane_ego_npc': [True, True, True, True],
            'back_ego_npc': [True, True, True, True],
        }
    
    NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE = {
        'time': [0.0, 0.1, 0.2, 0.3],
        'velocity_ego': [12.0, 11.999602538695664, 11.998449099520837, 11.993527898984228],
        'velocity_npc': [0.0, 0.0, 0.0, 0.0],
        # M/S^2 or G?
        'acceleration_ego': [1.0, 1.0, 1.0, 1.0],
        'acceleration_npc': [0.0, 0.0, 0.0, 0.0],
        # TODO What do we put here? None? Nan? Inf? -Inf?
        'relative_distance_ego_npc': [np.inf, np.inf, np.inf, np.inf],
        # TODO What do we put here? None? Nan? Inf? -Inf?
        # Is dist_long the same as relative dist?
        'dist_lon_ego_npc': [np.inf, np.inf, np.inf, np.inf],
        'same_lane_ego_npc': [False, False, False, False],
        # TODO What's the definition of this metric?
        'back_ego_npc': [False, False, False, False]
    }

    # Make those tests parametric?
    
    # TTC
    def test_ttc_two_vehicles_on_the_same_lane(self):
        # INSTANTIATE THE UNIT
        runtime_monitor = _instantiate_the_runtime_monitor_for("ttc")

        # SET EXPECTATIONS    
        expected_robustness = _compute_expected_robustness_of_criticality_metric(
            TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE, "ttc")

        # CALL THE RUNTIME MONITOR
        actual_robustness = runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])

    def test_ttc_vehicles_not_in_the_same_lane(self):
        # INSTANTIATE THE UNIT
        runtime_monitor = _instantiate_the_runtime_monitor_for("ttc")

        # SET EXPECTATIONS    
        expected_robustness = _compute_expected_robustness_of_criticality_metric(
            TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE, "ttc")

        # CALL THE RUNTIME MONITOR
        actual_robustness = runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])
    
    # RSS
    def test_rss_two_vehicles_on_the_same_lane(self):
         # INSTANTIATE THE UNIT
        runtime_monitor = _instantiate_the_runtime_monitor_for("rss")

        # SET EXPECTATIONS    
        expected_robustness = expected_robustness = _compute_expected_robustness_of_criticality_metric(
            TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE, "rss")

        # CALL THE RUNTIME MONITOR
        actual_robustness = runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])

    def test_rss_vehicles_not_in_the_same_lane(self):
         # INSTANTIATE THE UNIT
        runtime_monitor = _instantiate_the_runtime_monitor_for("rss")

        # SET EXPECTATIONS    
        expected_robustness = expected_robustness = _compute_expected_robustness_of_criticality_metric(
            TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE, "rss")

        # CALL THE RUNTIME MONITOR
        actual_robustness = runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])

    # MTTC
    def test_modified_ttc_two_vehicles_on_the_same_lane(self):
        # INSTANTIATE THE UNIT
        runtime_monitor = _instantiate_the_runtime_monitor_for("mttc")

        # SET EXPECTATIONS    
        expected_robustness = _compute_expected_robustness_of_criticality_metric(
            TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE, "mttc")

        # CALL THE RUNTIME MONITOR
        actual_robustness = runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_SAME_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])

    def test_modified_ttc_vehicles_not_in_the_same_lane(self):
        # INSTANTIATE THE UNIT
        runtime_monitor = _instantiate_the_runtime_monitor_for("mttc")

        # SET EXPECTATIONS    
        expected_robustness = _compute_expected_robustness_of_criticality_metric(
            TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE, "mttc")

        # CALL THE RUNTIME MONITOR
        actual_robustness = runtime_monitor.evaluate(TestAdCriticalityMetrics.NPC_PARKED_IN_FRONT_OF_TRAVELING_EGO_DIFFERENT_LANE)

        # ASSERT ROBUSTNESS [same time] -> [same value]
        # TODO Possibly a test smell (roulette assertion), but there's no assertAlmostEqual for lists od lists
        # assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]
        for expected_robustness_value, actual_robustness_value in zip(expected_robustness, actual_robustness):
            self.assertAlmostEqual(expected_robustness_value[1], actual_robustness_value[1])
   
if __name__ == '__main__':
    unittest.main()
