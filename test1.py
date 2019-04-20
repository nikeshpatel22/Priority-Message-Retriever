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

        print('\n')

    def test_logging_with_no_priority(self):
        """
        Test logging the message, then reading the message
        """
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


if __name__ == '__main__':
    unittest.main()
