from scheduling_sim import PriorityPreemptiveScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestPriorityPreemptiveScheduler(TestSchedulingAlgorithm):
    """Test class for Priority Preemptive Scheduler (PRIOp).

    This test class inherits from `TestSchedulingAlgorithm` and specializes in testing
    the Priority Preemptive scheduling algorithm. It includes specific expected results
    for Priority Preemptive scenarios.

    Attributes:
        Scheduler (type): The class to be tested (PriorityPreemptiveScheduler).
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

    Scheduler = PriorityPreemptiveScheduler

    # results
    average_wait_times = [2.8, 5.2, 5.4]
    average_turnaround_times = [5.6, 8.6, 8.6]
    total_execution_times = [14, 17, 16]
