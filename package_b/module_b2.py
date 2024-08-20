# package_b/module_b1.py

import datetime
import logging
import os
logger = logging.getLogger(__name__)


def process_log(p_off):
    for x in range(0, 100):
        d = datetime.datetime.now()
        t_str = '你好test' * 2
        logger.info('{}:{}:p_off({}):pid({})'.format(t_str, d.strftime('%Y-%m-%d %H:%M:%S'), p_off, os.getpid()))