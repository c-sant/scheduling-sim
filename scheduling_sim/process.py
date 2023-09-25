from enum import Enum

from scheduling_sim.exceptions import InvalidProcessNameError


class ProcessStatus(Enum):
    """Enumerator representing the status of a process.

    Attributes:
        READY (str): The process is ready to execute.
        WAITING (str): The process is waiting to execute.
        INTERRUPTED (str): The process execution was interrupted.
        RUNNING (str): The process is currently executing.
        TERMINATED (str): The process has completed execution.
    """

    READY = "Ready"
    """The process is ready to execute."""

    WAITING = "Waiting"
    """The process is waiting to execute."""

    INTERRUPTED = "Interrupted"
    """The process execution was interrupted."""

    RUNNING = "Running"
    """The process is currently executing."""

    TERMINATED = "Terminated"
    """The process has completed execution."""


class Process:
    """The representation of a computer process.

    A process as a lower-level concept is frequently associated with Operational
    Systems. It's a program in the state of execution, and have it's own memory
    space, system resources and execution context.

    Methods:
        reset(): Resets the process attributes for scheduling.
        run(): Changes the process status to `running`.
        wait(): Changes the process status to `waiting`.
        interrupt(): Changes the process status to `interrupted`.
        conclude(): Changes the process status to `terminated`.

    Properties:
        name (str): The name of the process.
        execution_time (int): The time required for the process to complete execution.
        priority_level (int): The priority level of the process.
        arrival_time (int): The time at which the process arrives and becomes ready
        for execution.
        conclusion_time (int): The instant when the process is concluded.
        wait_time (int): The time the process has spent waiting in the ready queue.
        remaining_execution_time (int): The time remaining for the process to complete
        turnaround_time (int): The interval between arrival and completion time.
        execution.
        enqueue_time (int): The time when the process is enquede in the ready queue.
        status (ProcessStatus): The status of the process.
        is_ready (bool): Whether the process is in the ready state.
        is_running (bool): Whether the process is in the running state.
        is_waiting (bool): Whether the process is in the waiting state.
        was_interrupted (bool): Whether the process was interrupted.
        is_terminated (bool): Whether the process is terminated.
        quantum_progress (int): The progress made within the quantum time slice.
    """

    def __init__(
        self,
        name: str,
        execution_time: int = 1,
        priority_level: int = 1,
        arrival_time: int = 0,
    ):
        self.name = name
        self.execution_time = execution_time
        self.priority_level = priority_level
        self.arrival_time = arrival_time

        self.reset()

    def __repr__(self) -> str:
        return f"Process({self.name})"

    def reset(self):
        """Resets the process properties for scheduling."""

        self.conclusion_time = self.arrival_time + self.execution_time
        self.enqueue_time = self.arrival_time
        self.remaining_execution_time = self.execution_time
        self._quantum_progress = 0
        self._status = ProcessStatus.READY

    # Process attributes

    @property
    def name(self) -> str:
        """str: The name of the process."""
        return self._name

    @name.setter
    def name(self, value: str) -> str:
        """Sets the name of the process.

        Args:
            value (str): The name to set.

        Raises:
            InvalidProcessNameError: If the name is empty.
        """

        value = str(value).strip()

        if value == "":
            raise InvalidProcessNameError(value)

        self._name = str(value)

    @property
    def priority_level(self) -> int:
        """int: The priority level of the process, used by scheduling algorithms."""
        return self._priority_level

    @priority_level.setter
    def priority_level(self, value: int):
        """Sets the priority level of the process.

        Args:
            value (int): The priority level to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 1.
        """

        if type(value) != int:
            raise TypeError(
                f"Priority level should be an integer. Got {type(value)} instead."
            )

        if value < 1:
            raise ValueError(
                f"Priority level should be higher than 0. Got {value} instead."
            )

        self._priority_level = value

    # Execution attributes

    @property
    def execution_time(self) -> int:
        """int: The time required for the process to complete execution."""
        return self._execution_time

    @execution_time.setter
    def execution_time(self, value: int):
        """Sets the execution time of the process.

        Args:
            value (int): The execution time to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 1.
        """

        if type(value) != int:
            raise TypeError(
                f"Process execution time should be an integer. Got {type(value)} instead."
            )

        if value < 1:
            raise ValueError(
                f"Execution time should be higher than 0. Got {value} instead."
            )

        self._execution_time = value

    @property
    def arrival_time(self) -> int:
        """int: The instant when the process arrives and becomes ready for execution."""
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value: int):
        """Sets the arrival time of the process.

        Args:
            value (int): The arrival time to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """

        if type(value) != int:
            raise TypeError(
                f"Arrival time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(f"Arrival time should be positive. Got {value} instead.")

        self._arrival_time = value

    @property
    def conclusion_time(self) -> int:
        """int: The instant when the process is concluded."""
        return self._conclusion_time

    @conclusion_time.setter
    def conclusion_time(self, value: int):
        """Sets the conclusion time of the process.

        Args:
            value (int): The conclusion time to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """

        if type(value) != int:
            raise TypeError(
                f"Conclusion time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(
                f"Conclusion time should be positive. Got {value} instead."
            )

        self._conclusion_time = value

    @property
    def wait_time(self) -> int:
        """int: The time the process has spent waiting in the ready queue."""
        return self.turnaround_time - self.execution_time

    @property
    def remaining_execution_time(self) -> int:
        """int: The time remaining for the process to complete execution."""
        return self._remaining_execution_time

    @remaining_execution_time.setter
    def remaining_execution_time(self, value: int):
        """Sets the remaining execution time of the process.

        Args:
            value (int): The remaining execution time to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """

        if type(value) != int:
            raise TypeError(
                f"Remaining execution time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(
                f"Remaining execution time should be positive. Got {value} instead."
            )

        self._remaining_execution_time = value

    @property
    def turnaround_time(self) -> int:
        """int: The interval between arrival and completion time."""
        return self.conclusion_time - self.arrival_time

    @property
    def enqueue_time(self) -> int:
        return self._enqueue_time

    @enqueue_time.setter
    def enqueue_time(self, value: int):
        if type(value) != int:
            raise TypeError(
                f"Enqueue time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(f"Enqueue time should be positive. Got {value} instead.")

        self._enqueue_time = value

    @property
    def quantum_progress(self):
        """int: The progress made within the current quantum."""
        return self._quantum_progress

    @quantum_progress.setter
    def quantum_progress(self, value: int):
        """The progress made within the current quantum.

        Args:
            value (int): The quantum progress value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if type(value) != int:
            raise TypeError(
                f"Quantum progress should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(
                f"Quantum progress should be positive. Got {value} instead."
            )

        self._quantum_progress = value

    # Status attributes

    @property
    def status(self) -> ProcessStatus:
        """ProcessStatus: The status of the process."""
        return self._status

    @property
    def is_ready(self) -> bool:
        """bool: Whether the process is in the `ready` state."""
        return self.status == ProcessStatus.READY

    @property
    def is_running(self) -> bool:
        """bool: Whether the process is in the `running` state."""
        return self.status == ProcessStatus.RUNNING

    @property
    def is_waiting(self) -> bool:
        """bool: Whether the process is in the `waiting` state."""
        return self.status == ProcessStatus.WAITING

    @property
    def was_interrupted(self):
        """bool: Whether the process is in the `interrupted` state."""
        return self.status == ProcessStatus.INTERRUPTED

    @property
    def is_terminated(self):
        """bool: Whether the process is in the `terminated` state."""
        return self.status == ProcessStatus.TERMINATED

    def run(self):
        """Changes the process status to `running`."""
        self._status = ProcessStatus.RUNNING

    def wait(self):
        """Changes the process status to `waiting`."""
        self._status = ProcessStatus.WAITING

    def interrupt(self):
        """Changes the process status to `interrupted`."""
        self._status = ProcessStatus.INTERRUPTED

    def conclude(self):
        """Changes the process status to `terminated`."""
        self._status = ProcessStatus.TERMINATED
