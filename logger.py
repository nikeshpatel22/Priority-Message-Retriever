from queue import LifoQueue
import datetime
import time

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

    def log(self, message, priority=1):
        """
        Logs the message into the correct queue

        Parameters
        ----------
        priority : int
            priority level of the message
        message : str
            message to be logged
        """

        timestamp = time.time()
        st = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        temp_list = [priority, st, message]

        if priority == 1:
            self.priorityOne.put(temp_list)
        if priority == 2:
            self.priorityTwo.put(temp_list)
        if priority == 3:
            self.priorityThree.put(temp_list)

        # if priority is above 3 include in priority 3 queue
        # else if priority is below 1, include in priority 1 queue
        if priority > 3:
            temp_list[0] = 3
            self.priorityThree.put(temp_list)
        elif priority < 1:
            temp_list[0] = 1
            self.priorityOne.put(temp_list)
