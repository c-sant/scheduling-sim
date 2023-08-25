class Process:
    """The representation of a program in execution, a process is a lower-level
    concept associated with Operational Systems. They have their own memory space,
    system resources and execution context.

    In this implementation of a Scheduling simulation, an object of type Process
    has a duration (the time it takes to be executed), a priority level and an
    arrival time, which represents the moment the Process was added to the Scheduler's
    queue.
    """

    def __init__(
        self, duration: int = 0, priority_level: int = 1, arrival_time: int = 0
    ):
        self.duration = duration
        self.priority_level = priority_level
        self.arrival_time = arrival_time

    def __repr__(self) -> str:
        return (
            "Process("
            f"duration={self.duration}, "
            f"priority_level={self.priority_level}, "
            f"arrival_time={self.arrival_time}"
            ")"
        )

    @property
    def duration(self) -> int:
        """The execution time of the process."""
        return self._duration

    @duration.setter
    def duration(self, value: int):
        if type(value) != int:
            raise TypeError(
                f"process duration should be an integer. Got {type(value)} instead."
            )

        self._duration = value

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
