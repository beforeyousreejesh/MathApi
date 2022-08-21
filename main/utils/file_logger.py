import logging

logging.basicConfig(filename='mathApi.log',filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def info(message):
    logging.info(message)

def error(message):
    logging.error(message)

def warning(message):
    logging.warning(message)