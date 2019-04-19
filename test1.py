from logger import *
from logReader import *
from queue import LifoQueue
import unittest


class TestLogging(unittest.TestCase):
    """
    Our basic test class
    """

    def test_logging(self):
        """
        Test logging the message, then reading the message
        """
        logger = Logger()
        logger.log(1, 'abc')
        logger.log(2, 'def')
        logger.log(1, 'ghi')

        logReader = LogReader(logger)
        message = logReader.get()
        self.assertEqual(message, 'def')
        message = logReader.get()
        self.assertEqual(message, 'ghi')
        message = logReader.get()
        self.assertEqual(message, 'abc')
        message = logReader.get()
        self.assertEqual(message, 'no messages')


if __name__ == '__main__':
    unittest.main()
