# package_a/module_a1.py

import logging

logger = logging.getLogger(__name__)

def function_a1():
    logger.debug("function_a1 开始执行")
    logger.info("正在处理一些任务...")
    logger.warning("这是一个警告！")
    logger.debug("function_a1 结束执行")
