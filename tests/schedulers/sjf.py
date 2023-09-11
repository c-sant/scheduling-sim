from scheduling_sim import ShortestJobFirstScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestShortestJobFirstScheduler(TestSchedulingAlgorithm):
    Scheduler = ShortestJobFirstScheduler

    # results
    average_wait_times = [3.0, 4.2, 4.4]
    average_turnaround_times = [5.8, 7.6, 7.6]
    total_execution_times = [14, 17, 16]
