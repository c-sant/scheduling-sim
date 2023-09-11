from scheduling_sim import FirstComeFirstServeScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestFirstComeFirstServeScheduler(TestSchedulingAlgorithm):
    Scheduler = FirstComeFirstServeScheduler

    # results
    average_wait_times = [5.2, 6, 5.2]
    average_turnaround_times = [8.0, 9.4, 8.4]
    total_execution_times = [14, 17, 16]
