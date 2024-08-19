# package_b/module_b1.py

import logging

logger = logging.getLogger(__name__)

def function_b1():
    logger.debug("function_b1 开始执行")
    logger.error("这是一个错误！")
    logger.critical("这是一个严重的错误！")
    logger.debug("function_b1 结束执行")
