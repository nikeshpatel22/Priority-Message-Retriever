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
