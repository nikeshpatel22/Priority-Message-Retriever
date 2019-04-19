import queue
from logger import *

class LogReader(Logger):
    """
    A class used to read log messages

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
    get()
        prints the correct log message, highest priority first
    """

    def __init__(self, logger_variables):
        """
        initialize queues

        Parameters
        ----------
        logger_variables: Logger
            Instance of Logger class that contains all the queues
        """

        self.priorityOne = logger_variables.priorityOne
        self.priorityTwo = logger_variables.priorityTwo
        self.priorityThree = logger_variables.priorityThree

    def get(self):
        """
        prints highest priority message

        Parameters
        ----------
        no parameters
        """

        if self.priorityThree.empty() == False:
            message = self.priorityThree.get()
            print(message)
            return
        if self.priorityTwo.empty() == False:
            message = self.priorityTwo.get()
            print(message)
            return
        if self.priorityOne.empty() == False:
            message = self.priorityOne.get()
            print(message)
            return
        else:
            print("no messages")
