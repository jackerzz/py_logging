import logging
import datetime
import os
from multiprocessing import Pool,Process
import time
 

class MPFileLogHandler(logging.Handler):
    def __init__(self, file_path):
        self._fd = os.open(file_path, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
        logging.Handler.__init__(self)

    def emit(self, record):
        msg = "{}\n".format(self.format(record))
        os.write(self._fd, msg.encode('utf-8'))

# 文件日志处理器
logger_file_handler = MPFileLogHandler('one_file_log_2.log')
# 控制台日志处理器
logger_console_handler = logging.StreamHandler()
logger = logging.getLogger('test')
logger.addHandler(logger_file_handler)
logger.addHandler(logger_console_handler)
logger.setLevel(logging.DEBUG)
# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger_file_handler.setFormatter(formatter)
logger_console_handler.setFormatter(formatter)

from d import run

if __name__ == '__main__':
	# 多进程写日志
    run()
    