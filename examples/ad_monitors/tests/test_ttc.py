import pytest
import rtamt
import numpy as np

def robustness_of_tcc_measure(velocity_ego: float, velocity_npc: float, relative_distance_ego_npc: float, same_lane_ego_npc: bool):
    safe_ttc = 3.5

    same_lane_ego_npc_as_float = np.PINF if same_lane_ego_npc else np.NINF

    cond = min(same_lane_ego_npc_as_float, velocity_ego - velocity_npc) * np.PINF

    # cond -> ((relative_distance_ego_npc / (velocity_ego - velocity_npc)) >= safe_ttc)
    return max( - cond, (relative_distance_ego_npc / (velocity_ego - velocity_npc)) - safe_ttc);


def compute_expected_robustness(dataSet: dict):
    expected_robustness = []
    for i in range(0, len(dataSet["time"])):
        time = dataSet["time"][i]
        velocity_ego = dataSet["velocity_ego"][i]
        velocity_npc = dataSet["velocity_npc"][i]
        relative_distance_ego_npc = dataSet["relative_distance_ego_npc"][i]
        same_lane_ego_npc = dataSet["same_lane_ego_npc"][i]

        expected_robustness.append([time, robustness_of_tcc_measure(velocity_ego, velocity_npc, relative_distance_ego_npc, same_lane_ego_npc)])

    return expected_robustness

def test_smoke(tcc_runtime_monitor: rtamt.StlDiscreteTimeSpecification):
    dataSet = {
        'time': [0.0, 0.1, 0.2, 0.3],
        'velocity_ego': [12.0, 11.999602538695664, 11.998449099520837, 11.993527898984228],
        'velocity_npc': [0.0, 0.0, 0.0, 0.0],
        'relative_distance_ego_npc': [66.4227170936, 65.22273038996738, 64.02282178214598, 62.823166528097175],
        'same_lane_ego_npc': [True, True, True, True]
    }

    # SET EXPECTATIONS    
    expected_robustness = compute_expected_robustness(dataSet)

    # CALL THE RUNTIME MONITOR
    actual_robustness = tcc_runtime_monitor.evaluate(dataSet)

    # ASSERT ROBUSTNESS [same time] -> [same value]
    assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]




def test_vehicles_not_in_the_same_line(tcc_runtime_monitor: rtamt.StlDiscreteTimeSpecification):
    dataSet = {
        'time': [0.0, 0.1, 0.2, 0.3],
        'velocity_ego': [12.0, 11.999602538695664, 11.998449099520837, 11.993527898984228],
        'velocity_npc': [0.0, 0.0, 0.0, 0.0],
        'relative_distance_ego_npc': [np.inf, np.inf, np.inf, np.inf],
        'same_lane_ego_npc': [False, False, False, False]
    }
 
    # SET EXPECTATIONS    
    expected_robustness = compute_expected_robustness(dataSet)

    # CALL THE RUNTIME MONITOR
    actual_robustness = tcc_runtime_monitor.evaluate(dataSet)

    # ASSERT ROBUSTNESS
    assert actual_robustness == [ [er[0], pytest.approx(er[1])] for er in expected_robustness]


# @pytest.mark.skip()
# def test_smoke(tcc_runtime_monitor: rtamt.StlDiscreteTimeSpecification):
#     dataSet = {
#         'time': [0.0, 0.1, 0.2, 0.3],
#         'velocity_ego': [12.0, 11.999602538695664, 11.998449099520837, 11.993527898984228],
#         'velocity_npc': [0.0, 0.0, 0.0, 0.0],
#         'relative_distance_ego_npc': [66.4227170936, 65.22273038996738, 64.02282178214598, 62.823166528097175],
#         'same_lane_ego_npc': [True, True, True, True]
#     }
 
#     # CALL THE RUNTIME MONITOR
#     actual_robustness = tcc_runtime_monitor.evaluate(dataSet)
#     # ASSERT ROBUSTNESS

#     print(f"{actual_robustness}")
