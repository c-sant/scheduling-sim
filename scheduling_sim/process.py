class Process:
    """The representation of a program in execution, a process is a lower-level
    concept associated with Operational Systems. They have their own memory space,
    system resources and execution context.

    In this implementation of a Scheduling simulation, an object of type Process
    has an execution time (the time it takes to be executed), a priority level and
    an arrival time, which represents the moment the Process was added to the Scheduler's
    queue.
    """

    def __init__(
        self, execution_time: int = 0, priority_level: int = 1, arrival_time: int = 0
    ):
        self.execution_time = execution_time
        self.total_runtime = execution_time
        self.priority_level = priority_level
        self.arrival_time = arrival_time

    def __repr__(self) -> str:
        return (
            "Process("
            f"execution_time={self.execution_time}, "
            f"priority_level={self.priority_level}, "
            f"arrival_time={self.arrival_time}"
            ")"
        )

    @property
    def execution_time(self) -> int:
        """The execution time (duration) of the process."""
        return self._execution_time

    @execution_time.setter
    def execution_time(self, value: int):
        if type(value) != int:
            raise TypeError(
                f"process execution time should be an integer. Got {type(value)} instead."
            )

        self._execution_time = value

    @property
    def priority_level(self) -> int:
        """The level of priority a process has in a schedule."""
        return self._priority_level

    @priority_level.setter
    def priority_level(self, value: int):
        if type(value) != int:
            raise TypeError(
                f"priority level should be an integer. Got {type(value)} instead."
            )

        if value < 1:
            raise ValueError(
                f"priority level should be higher than 0. Got {value} instead."
            )

        self._priority_level = value

    @property
    def arrival_time(self) -> int:
        """The instant the process should be added to the schedule's job queue."""
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value: int):
        if type(value) != int:
            raise TypeError(
                f"arrival time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(f"arrival time should be positive. Got {value} instead.")

        self._arrival_time = value

    @property
    def total_runtime(self) -> int:
        """The total runtime the process needed to finish (execution time + waiting)."""
        return self._total_runtime

    @total_runtime.setter
    def total_runtime(self, value: int):
        if type(value) != int:
            raise TypeError(
                f"total runtime should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(f"total runtime should be positive. Got {value} instead.")

        if value < self.execution_time:
            raise ValueError("total runtime should not be lower than execution time.")

        self._total_runtime = value
