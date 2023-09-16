from scheduling_sim import ShortestJobFirstScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm


class TestShortestJobFirstScheduler(TestSchedulingAlgorithm):
    """Test Class for Shortest Job First (SJF) Scheduler.

    This test class inherits from `TestSchedulingAlgorithm` and specializes in testing
    the Shortest Job First (SJF) scheduling algorithm. It includes specific expected results
    for SJF scenarios.
    
    Attributes:
        Scheduler (type): The class to be tested, which is the SJF scheduler.
        average_wait_times (list): A list of expected average wait times for SJF test cases.
        average_turnaround_times (list): A list of expected average turnaround times
        for SJF test cases.
        total_execution_times (list): A list of expected total execution times for SJF test 
        cases.
    """
    
    Scheduler = ShortestJobFirstScheduler

    # results
    average_wait_times = [3.0, 4.2, 4.4]
    average_turnaround_times = [5.8, 7.6, 7.6]
    total_execution_times = [14, 17, 16]
