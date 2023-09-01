from os.path import join
from loguru import logger

from spider.config import Config as cfg

def confure_logger():
    logger.add(join(cfg.LOGDIR, "app.log"))