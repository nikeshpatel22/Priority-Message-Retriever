from queue import LifoQueue
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
        initialize queues, prints header for logs

        Parameters
        ----------
        logger_variables: Logger
            Instance of Logger class that contains all the queues
        """

        self.priorityOne = logger_variables.priorityOne
        self.priorityTwo = logger_variables.priorityTwo
        self.priorityThree = logger_variables.priorityThree

        print("Priority    Timestamp                 Message")
        print("---------------------------------------------")

    def get(self):
        """
        prints highest priority message

        Parameters
        ----------
        no parameters
        """

        if self.priorityThree.empty() == False:
            message = self.priorityThree.get()
            print("{}           {}       {}".format(message[0], message[1], message[2]))
            return message[2]
        if self.priorityTwo.empty() == False:
            message = self.priorityTwo.get()
            print("{}           {}       {}".format(message[0], message[1], message[2]))
            return message[2]
        if self.priorityOne.empty() == False:
            message = self.priorityOne.get()
            print("{}           {}       {}".format(message[0], message[1], message[2]))
            return message[2]
        else:
            print("no messages")
            return "no messages"
