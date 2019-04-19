from queue import LifoQueue

class Logger:
    """
    A class used to log messages

    ...

    Attributes
    ----------
    priorityOne : queue(str)
        a queue of messages with priority level 1
    priorityTwo : queue(str)
        a queue of messages with priority level 2
    priorityThree : queue(str)
        a queue of messages with priority level 3

    Methods
    -------
    log(priority, message)
        logs the message into the correct queue
    """

    def __init__(self):
        """
        initialize queues

        Parameters
        ----------
        no parameters
        """

        self.priorityOne = LifoQueue()
        self.priorityTwo = LifoQueue()
        self.priorityThree = LifoQueue()

    def log(self, priority, message):
        """
        Logs the message into the correct queue

        Parameters
        ----------
        priority : int
            priority level of the message
        message : str
            message to be logged
        """

        if priority == 1:
            self.priorityOne.put(message)
        if priority == 2:
            self.priorityTwo.put(message)
        if priority == 3:
            self.priorityThree.put(message)
