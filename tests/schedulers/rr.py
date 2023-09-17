from scheduling_sim import RoundRobinScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestRoundRobinScheduler(TestSchedulingAlgorithm):
    Scheduler = RoundRobinScheduler

    # results
    average_wait_times = [5.6, 8.2, 6.8]
    average_turnaround_times = [8.4, 11.6, 10]
    total_execution_times = [14, 17, 16]
