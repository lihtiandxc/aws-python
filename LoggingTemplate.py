import logging
import json
import os

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))

def lambda_handler(event, context):

    logger.info('test')
    logger.info("event: {}".format(event))
    logger.info("context: {}".format(context))
