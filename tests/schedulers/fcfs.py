from scheduling_sim import FirstComeFirstServeScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestFirstComeFirstServeScheduler(TestSchedulingAlgorithm):
    """Test Class for First-Come-First-Serve Scheduler (FCFS).

    This test class inherits from `TestSchedulingAlgorithm` and specializes in testing
    the FCFS scheduling algorithm. It includes specific expected results for FCFS scenarios.

    Attributes:
        Scheduler (type): The class to be tested (FirstComeFirstServeScheduler).
        average_wait_times (list): A list of expected average wait times for test cases.
        average_turnaround_times (list): A list of expected average turnaround times
        for test cases.
        total_execution_times (list): A list of expected total execution times for test
        cases.

    Methods:
        case_1(self) -> Scheduler: Defines the first test case scenario and returns a scheduler.
        case_2(self) -> Scheduler: Defines the second test case scenario and returns a scheduler.
        case_3(self) -> Scheduler: Defines the third test case scenario and returns a scheduler.
        get_scheduler(self, case_id: int) -> Scheduler: Returns a scheduler based on the
        selected case.
        test_average_wait_time(self, case_id: int): Test for average wait time.
        test_average_turnaround_time(self, case_id: int): Test for average turnaround time.
        test_total_execution_time(self, case_id: int): Test for total execution time.
    """

    Scheduler = FirstComeFirstServeScheduler

    # results
    average_wait_times = [5.2, 6, 5.2]
    average_turnaround_times = [8.0, 9.4, 8.4]
    total_execution_times = [14, 17, 16]
