from scheduling_sim import FirstComeFirstServeScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestFirstComeFirstServeScheduler(TestSchedulingAlgorithm):
    """Test Class for First-Come-First-Serve (FCFS) Scheduler.

    This test class inherits from `TestSchedulingAlgorithm` and specializes in testing
    the FCFS scheduling algorithm. It includes specific expected results for FCFS scenarios.

    Attributes:
        Scheduler (type): The class to be tested, which is the FCFS scheduler.
        average_wait_times (list): A list of expected average wait times for FCFS test cases.
        average_turnaround_times (list): A list of expected average turnaround times
        for FCFS test cases.
        total_execution_times (list): A list of expected total execution times for FCFS
        test cases.
    """

    Scheduler = FirstComeFirstServeScheduler

    # results
    average_wait_times = [5.2, 6, 5.2]
    average_turnaround_times = [8.0, 9.4, 8.4]
    total_execution_times = [14, 17, 16]
