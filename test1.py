from logger import *
from logReader import *
from queue import LifoQueue
import unittest
import time


class TestLogging(unittest.TestCase):
    """
    Our basic test class
    """

    def test_logging_1(self):
        """
        Test logging the message, then reading the message
        """

        print("TEST-1 -------------------------------------")

        logger = Logger()
        logger.log('abc', 1)
        time.sleep(5)
        logger.log('def', 2)
        time.sleep(5)
        logger.log('ghi', 1)

        logReader = LogReader(logger)
        message = logReader.get()
        self.assertEqual(message, 'def')
        message = logReader.get()
        self.assertEqual(message, 'ghi')
        message = logReader.get()
        self.assertEqual(message, 'abc')
        message = logReader.get()
        self.assertEqual(message, 'no messages')

    def test_logging_with_no_priority(self):
        """
        Test logging the message with no priority, then reading the message
        """

        print("TEST-2 -------------------------------------")

        logger = Logger()
        logger.log('hello')
        logger.log('abc', 3)
        logger.log('def', 2)
        logger.log('ghi', 2)

        logReader = LogReader(logger)
        message = logReader.get()
        self.assertEqual(message, 'abc')
        message = logReader.get()
        self.assertEqual(message, 'ghi')
        message = logReader.get()
        self.assertEqual(message, 'def')
        message = logReader.get()
        self.assertEqual(message, 'hello')

    def test_no_logs(self):
        """
        Test logging no messages, then reading the logs
        """

        print("TEST-3 -------------------------------------")

        logger = Logger()
        logReader = LogReader(logger)
        message = logReader.get()
        self.assertEqual(message, 'no messages')
        message = logReader.get()
        self.assertEqual(message, 'no messages')

    def test_wrong_priority(self):
        """
        Test logging messages with invalid priority, then reading the logs
        """

        print("TEST-4 -------------------------------------")

        logger = Logger()
        logger.log('hello')
        logger.log('abc', 5)
        logger.log('def', 2)
        logger.log('ghi', 3)
        logger.log('bye', 0)

        logReader = LogReader(logger)
        message = logReader.get()
        self.assertEqual(message, 'ghi')
        message = logReader.get()
        self.assertEqual(message, 'abc')
        message = logReader.get()
        self.assertEqual(message, 'def')
        message = logReader.get()
        self.assertEqual(message, 'bye')
        message = logReader.get()
        self.assertEqual(message, 'hello')

if __name__ == '__main__':
    unittest.main()
