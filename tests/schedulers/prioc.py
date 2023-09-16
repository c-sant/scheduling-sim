from scheduling_sim import PriorityCooperativeScheduler

from .scheduling_algorithm import TestSchedulingAlgorithm

class TestPriorityCooperativeScheduler(TestSchedulingAlgorithm):
    """Test Class for Priority Cooperative Scheduler.

    This test class inherits from `TestSchedulingAlgorithm` and specializes in testing
    the Priority Cooperative scheduling algorithm. It includes specific expected results
    for Priority Cooperative scenarios.
    
    Attributes:
        Scheduler (type): The class to be tested, which is the Priority Cooperative scheduler.
        average_wait_times (list): A list of expected average wait times for Priority Cooperative
        test cases.
        average_turnaround_times (list): A list of expected average turnaround times for 
        Priority Cooperative test cases.
        total_execution_times (list): A list of expected total execution times for Priority 
        Cooperative test cases.
    """
    
    Scheduler = PriorityCooperativeScheduler
    
    # results
    average_wait_times = [3.8, 4.6, 5.2]
    average_turnaround_times = [6.6, 8.0, 8.4]
    total_execution_times = [14, 17, 16]