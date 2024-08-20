import logging
import os

import datetime
import time
from multiprocessing import Pool,Process

logger = logging.getLogger(__name__)
def process_log(p_off):
    for x in range(0, 5):
        d = datetime.datetime.now()
        t_str = '你好test' * 2
        time.sleep(1)
        logger.info('{}:{}:p_off({}):pid({})'.format(t_str, d.strftime('%Y-%m-%d %H:%M:%S'), p_off, os.getpid()))

def run():
    for i in range(4):
        p = Process(target=process_log, args=(i, ))
    p.start()
    p.join()
    
def rune():
     # 多进程写日志
    p = Pool(4)
    for i in range(4):
        p.apply_async(process_log, args=(i,))
    print('waiting.....')
    p.close()
    p.join()
    print('done.....')