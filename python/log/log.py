import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.warning('just for warning')
logging.info('Starting program')
logging.info('Trying to devide 1 by 0')
print(1/0)

logging.info('The division succeeded')
logging.info('Ending program')
