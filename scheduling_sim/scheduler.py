from enum import Enum, auto

from scheduling_sim.exceptions import (
    InvalidProcessQueueError,
    NoProcessesInQueueError,
    NoProcessWithArrivalTimeZeroError,
)
from scheduling_sim.process import Process


class SchedulingAlgorithm(Enum):
    """Enumeration of scheduling algorithms for process scheduling.

    This enumeration defines constants for various scheduling algorithms
    that can be used in process scheduling.

    Constants:
        FCFS (int): First-Come-First-Serve.
        SJF (int): Shortest Job First.
        SRTF (int): Shortest Remaining Time First.
        RR (int): Round Robin.
        PRIOp (int): Preemptive Priority.
        PRIOc (int): Non-Preemptive Priority.

    Each constant represents a specific scheduling algorithm.

    Examples:
        To use the FCFS scheduling algorithm, you can do the following:

        >>> algorithm = SchedulingAlgorithm.FCFS
    """

    FCFS = auto()
    """First-Come-First-Serve.
    
    Non-preemptive algorithm that executes processes in the order they arrive,
    regardless of their priority level. 
    """

    SJF = auto()
    """Shortest Job First.
    
    Non-preemptive algorithm that selects the process with the shortest execution 
    time from the process queue next. It usually minimizes average waiting time.
    """

    SRTF = auto()
    """Shortest Remaining Time First.
    
    Preemptive version of SJF that selects the process with the shortest remaining
    execution time whenever a new process arrives or a running process yields.
    """

    RR = auto()
    """Round Robin.
    
    Each process gets a fixed time slice (quantum) to execute before being placed
    at the end of the queue.
    """

    PRIOp = auto()
    """Preemptive Priority.

    Preemptive algorithm that sleects the process with the highest priority level
    for execution. Being preemptive, more "important" processes interrupt lower-priority
    ones.
    """

    PRIOc = auto()
    """Non-Preemptive Priority.

    Non-preemptive algorithm that sleects the process with the highest priority level
    for execution when a running process finishes.
    """


class Scheduler:
    def __init__(self, processes: list[Process] = None):
        if processes == None:
            processes = []

        self._processes: list[Process] = []

        for process in processes:
            self.add_process(process)

        self._assert_queue_validity()
        self.reset()

    def __repr__(self) -> str:
        return f"Scheduler(Processes: {len(self._processes)})"

    @property
    def total_execution_time(self) -> int:
        if len(self._processes) == 0:
            return 0

        return sum([process.execution_time for process in self._processes])

    @property
    def process_queue_size(self) -> int:
        return len(self._processes)

    def add_process(self, process: Process):
        if type(process) != Process:
            raise InvalidProcessQueueError()

        self._processes.append(process)
        self._processes = sorted(self._processes, key=lambda x: x.arrival_time)

    def execute_scheduling(self, algorithm: SchedulingAlgorithm, *args, **kwargs):
        self._assert_queue_validity()

        if algorithm == SchedulingAlgorithm.FCFS:
            schedule = self.get_fcfs_schedule(*args, **kwargs)

        elif algorithm == SchedulingAlgorithm.SJF:
            schedule = self.get_sjf_schedule(*args, **kwargs)

        elif algorithm == SchedulingAlgorithm.SRTF:
            schedule = self.get_srtf_schedule(*args, **kwargs)

        elif algorithm == SchedulingAlgorithm.RR:
            schedule = self.get_rr_schedule(*args, **kwargs)

        elif algorithm == SchedulingAlgorithm.PRIOp:
            schedule = self.get_priority_schedule(preemptive=True, *args, **kwargs)

        elif algorithm == SchedulingAlgorithm.PRIOc:
            schedule = self.get_priority_schedule(preemptive=False, *args, **kwargs)

        else:
            raise ValueError(f"Unexpected schedule algorithm: '{algorithm}'.")

    def get_fcfs_schedule(self):
        raise NotImplementedError()

    def get_sjf_schedule(self):
        raise NotImplementedError()

    def get_srtf_schedule(self):
        raise NotImplementedError()

    def get_rr_schedule(self, quantum_limit: bool = 2):
        raise NotImplementedError()

    def get_priority_schedule(self, preemptive: bool):
        raise NotImplementedError()

    def reset(self):
        for process in self._processes:
            process.reset()

        self._current_running_process: Process | None = None

    def _assert_queue_validity(self):
        if len(self._processes) == 0:
            raise NoProcessesInQueueError()

        if self._processes[0].arrival_time != 0:
            raise NoProcessWithArrivalTimeZeroError()

    def _check_process_queue(self):
        if type(self._processes) != list:
            raise InvalidProcessQueueError()

        for process in self._processes:
            if type(process) != Process:
                raise InvalidProcessQueueError()
