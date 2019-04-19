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
        logger1 = Logger()
        logger.log(2, 'def')
        logger1.log(3, 'second')
        logger1.log(3, 'first')
        logger.log(1, 'ghi')
        logger1.log(2, 'last')

        logReader = LogReader(logger)
        logReader1 = LogReader(logger1)

        message = logReader.get()
        self.assertEqual(message, 'def')

        message = logReader1.get()
        self.assertEqual(message, 'first')

        message = logReader.get()
        self.assertEqual(message, 'ghi')

        message = logReader1.get()
        self.assertEqual(message, 'second')

        message = logReader.get()
        self.assertEqual(message, 'abc')

        message = logReader1.get()
        self.assertEqual(message, 'last')

        message = logReader.get()
        self.assertEqual(message, 'no messages')

        message = logReader1.get()
        self.assertEqual(message, 'no messages')


if __name__ == '__main__':
    unittest.main()
