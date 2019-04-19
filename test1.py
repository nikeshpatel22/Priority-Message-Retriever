from main import *
import queue

logger = Logger()
logger.log(1, 'abc')
logger.log(2, 'def')
logger.log(1, 'ghi')

logReader = LogReader(logger)
logReader.get()
logReader.get()
logReader.get()
logReader.get()
