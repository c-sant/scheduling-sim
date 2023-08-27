from enum import Enum

from scheduling_sim.exceptions import InvalidProcessNameError


class ProcessStatus(Enum):
    """Enum representing the status of a process.

    Attributes:
        READY (str): The process is ready to execute.
        WAITING (str): The process is waiting to execute.
        RUNNING (str): The process is currently executing.
        BLOCKED (str): The process is blocked and waiting for an event.
        TERMINATED (str): The process has completed execution.
    """

    READY = "ready"
    """The process is ready to execute."""

    WAITING = "waiting"
    """The process is waiting to execute."""

    RUNNING = "running"
    """The process is currently executing."""

    BLOCKED = "blocked"
    """The process is blocked and waiting for an event."""

    TERMINATED = "terminated"
    """The process has completed execution."""


class Process:
    """The representation of a program in execution, a process is a lower-level
    concept associated with Operational Systems. They have their own memory space,
    system resources and execution context.

    Attributes:
        name (str): The name of the process.
        execution_time (int): The time required for the process to complete execution.
        turnaround_time (int): The interval between arrival and completion time.
        priority_level (int): The priority level of the process, used in scheduling
        algorithms.
        arrival_time (int): The time at which the process arrives and becomes ready
        for execution.
        wait_time (int): The time the process has spent waiting in the ready queue.
        remaining_execution_time (int): The time remaining for the process to complete
        execution.
        status (ProcessStatus): The status of the process.
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
    def wait_time(self) -> int:
        """int: The time the process has spent waiting in the ready queue."""
        return self._wait_time

    @wait_time.setter
    def wait_time(self, value: int):
        """Sets the wait time of the process.

        Args:
            value (int): The wait time to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """

        if type(value) != int:
            raise TypeError(
                f"Wait time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(f"Wait time should be positive. Got {value} instead.")

        self._wait_time = value

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
        return self.execution_time + self.wait_time

    @property
    def status(self) -> ProcessStatus:
        """ProcessStatus: The status of the process."""
        return self._status

    @status.setter
    def status(self, value: ProcessStatus):
        """Sets the status of the process.

        Args:
            value (ProcessStatus): The status to set.

        Raises:
            ValueError: If the value is not a valid ProcessStatus enum.
        """

        if not isinstance(value, ProcessStatus):
            raise TypeError(
                f"Status should be a valid ProcessStatus value. Got {type(value)} instead."
            )

        self._status = value

    def reset(self):
        """Resets the process attributes for scheduling.

        This method resets the process's wait time, remaining execution time, and
        status to their initial values. After calling this method, the process is
        ready to be scheduled again.
        """

        self.wait_time = 0
        self.remaining_execution_time = self.execution_time
        self.status = ProcessStatus.READY
