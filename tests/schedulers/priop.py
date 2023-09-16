from scheduling_sim import PriorityPreemptiveScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestPriorityPreemptiveScheduler(TestSchedulingAlgorithm):
    Scheduler = PriorityPreemptiveScheduler

    # results
    average_wait_times = [2.8, 5.2, 5.4]
    average_turnaround_times = [5.6, 8.6, 8.6]
    total_execution_times = [14, 17, 16]
