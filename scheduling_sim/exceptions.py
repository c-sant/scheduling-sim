class NoProcessWithArrivalTimeZeroError(Exception):
    """Exception raised when none of the processes have an arrival time of 0.

    This exception is raised when a scheduling algorithm or process management code expects at least one
    process to have an arrival time of 0 but none of the processes meet this criteria.

    Attributes:
        message (str): A custom error message describing the exception.
    """

    def __init__(self, message="None of the processes have an arrival time of 0."):
        self.message = message
        super().__init__(self.message)


class NoProcessesInQueueError(Exception):
    """
    Exception raised when there are no processes in the queue.

    This exception is raised when a scheduling algorithm or process management code expects to operate
    on a queue of processes but encounters an empty queue.

    Attributes:
        message (str): A custom error message describing the exception.
    """

    def __init__(self, message="The queue does not contain any processes."):
        self.message = message
        super().__init__(self.message)
