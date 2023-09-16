from scheduling_sim import ShortestRemainingTimeFirstScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestShortestRemainingTimeFirstScheduler(TestSchedulingAlgorithm):
    Scheduler = ShortestRemainingTimeFirstScheduler

    # results
    average_wait_times = [2.6, 4.2, 3.6]
    average_turnaround_times = [5.4, 7.6, 6.8]
    total_execution_times = [14, 17, 16]
