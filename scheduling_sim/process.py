from scheduling_sim.exceptions import InvalidProcessNameError


class Process:
    """The representation of a program in execution, a process is a lower-level
    concept associated with Operational Systems. They have their own memory space,
    system resources and execution context.

    Attributes:
        name (str): The name of the process.
        execution_time (int): The time required for the process to complete execution.
        total_runtime (int): The total runtime of the process, which is the sum
        of execution and waiting time.
        priority_level (int): The priority level of the process, used in scheduling
        algorithms.
        arrival_time (int): The time at which the process arrives and becomes ready
        for execution.
        wait_time (int): The time the process has spent waiting in the ready queue.
        remaining_execution_time (int): The time remaining for the process to complete
        execution.
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

        self.wait_time = 0
        self.remaining_execution_time = self.execution_time

    def __repr__(self) -> str:
        return (
            "Process("
            f"name='{self.name}', "
            f"execution_time={self.execution_time}, "
            f"priority_level={self.priority_level}, "
            f"arrival_time={self.arrival_time}"
            ")"
        )

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
                f"process execution time should be an integer. Got {type(value)} instead."
            )

        if value < 1:
            raise ValueError(
                f"execution time should be higher than 0. Got {value} instead."
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
                f"priority level should be an integer. Got {type(value)} instead."
            )

        if value < 1:
            raise ValueError(
                f"priority level should be higher than 0. Got {value} instead."
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
                f"arrival time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(f"arrival time should be positive. Got {value} instead.")

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
                f"wait time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(f"wait time should be positive. Got {value} instead.")

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
                f"remaining execution time should be an integer. Got {type(value)} instead."
            )

        if value < 0:
            raise ValueError(
                f"remaining execution time should be positive. Got {value} instead."
            )

        self._remaining_execution_time = value

    @property
    def total_runtime(self) -> int:
        """int: The total runtime of the process, which is the sum of execution and waiting time."""
        return self.execution_time + self.wait_time
