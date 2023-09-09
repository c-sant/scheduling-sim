######################
# Process exceptions #
######################


class InvalidProcessNameError(ValueError):
    """
    Exception raised when an invalid process name is encountered.

    This exception is raised when a process name does not meet the required naming criteria.

    Attributes:
        message (str): A custom error message describing the exception.
        process_name (str): The invalid process name that triggered the exception.
    """

    def __init__(self, process_name, message="Invalid process name encountered."):
        """
        Initializes a new InvalidProcessNameError instance.

        Args:
            process_name (str): The invalid process name that triggered the exception.
            message (str, optional): A custom error message describing the exception. Defaults to a generic message.
        """
        self.process_name = process_name
        self.message = message
        super().__init__(self.message)


########################
# Scheduler exceptions #
########################


class NoProcessWithArrivalTimeZeroError(Exception):
    """Exception raised when none of the processes have an arrival time of 0.

    This exception is raised when a scheduling algorithm or process management code
    expects at least one process to have an arrival time of 0 but none of the processes
    meet this criteria.

    Attributes:
        message (str): A custom error message describing the exception.
    """

    def __init__(self, message="None of the processes have an arrival time of 0."):
        self.message = message
        super().__init__(self.message)


class NoProcessesInQueueError(Exception):
    """Exception raised when there are no processes in the queue.

    This exception is raised when a scheduling algorithm or process management code
    expects to operate on a queue of processes but encounters an empty queue.

    Attributes:
        message (str): A custom error message describing the exception.
    """

    def __init__(self, message="The queue does not contain any processes."):
        self.message = message
        super().__init__(self.message)


class InvalidProcessQueueError(TypeError):
    """Exception raised when the processes queue contains objects that are not of type Process.

    This exception is raised when a Scheduler attempts to operate on a processes
    queue that contains objects of an incorrect type.

    Attributes:
        message (str): A custom error message describing the exception.
    """

    def __init__(
        self,
        message="Invalid process queue. The queue must be a list and all elements must be of type Process.",
    ):
        self.message = message
        super().__init__(self.message)
