import queue

class logger:

    def __init_(self):
        self.priorityOne = queue.Queue()
        self.priorityTwo = queue.Queue()
        self.priorityThree = queue.Queue()

    def log(self, priority, message):
        if priority == 1:
            self.priorityOne.put(message)
        if priority == 2:
            self.priorityTwo.put(message)
        if priority == 3:
            self.priorityThree.put(message)

class logReader(logger):

    def __init__(self, logger_variables):
        self.priorityOne = logger_variables.priorityOne
        self.priorityTwo = logger_variables.priorityTwo
        self.priorityThree = logger_variables.priorityThree

    def get():
        if self.priorityOne.empty() == False:
            message = self.priorityOne.get()
            print(message)
            return
        if self.priorityTwo.empty() == False:
            message = self.priorityTwo.get()
            print(message)
            return
        if self.priorityThree.empty() == False:
            message = self.priorityThree.get()
            print(message)
            return
