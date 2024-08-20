# main.py
import os
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from logging.handlers import SMTPHandler

class RepeatFilter(logging.Filter):
    def __init__(self, threshold=3):
        super().__init__()
        self.threshold = threshold
        self.msg_count = {}

    def filter(self, record):
        msg = record.getMessage()
        if msg not in self.msg_count:
            self.msg_count[msg] = 0
        self.msg_count[msg] += 1

        # 只在消息出现达到 threshold 次后才返回 True，允许邮件发送
        if self.msg_count[msg] >= self.threshold:
            self.msg_count[msg] = 0  # 重置计数器
            return True
        return False
    
class MPFileLogHandler(logging.Handler):
    def __init__(self, file_path):
        self._fd = os.open(file_path, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
        logging.Handler.__init__(self)

    def emit(self, record):
        msg = "{}\n".format(self.format(record))
        os.write(self._fd, msg.encode('utf-8'))    

class NoDuplicateFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        self.logged = set()

    def filter(self, record):
        msg = record.getMessage()
        if msg in self.logged:
            return False
        self.logged.add(msg)
        return True
    
smtp_handler = SMTPHandler(
    mailhost=("smtp.qq.com", 465),  # QQ邮箱SMTP服务器
    fromaddr="your_qq_email@qq.com",  # 发件人邮箱地址
    toaddrs=["recipient1@example.com", "recipient2@example.com"],  # 收件人邮箱地址
    subject="Critical Error in My Project",  # 邮件主题
    credentials=("your_qq_email@qq.com", "your_smtp_auth_code"),  # QQ邮箱地址和授权码
    secure=()  # 使用SSL加密连接
)

# 轮转日志文件，每个文件最大10MB，保留3个旧文件
rotating_handler = RotatingFileHandler(
    'app.log', maxBytes=10*1024*1024, backupCount=3
)

# 按时间轮转日志文件，每天创建一个新文件，保留7天的日志
timed_rotating_handler = TimedRotatingFileHandler(
    'app.log', when='D', interval=1, backupCount=7
)

# 只发送ERROR及以上级别的日志
# smtp_handler.setLevel(logging.ERROR)  
# smtp_handler.addFilter(RepeatFilter(threshold=3))
# rotating_handler.addFilter(NoDuplicateFilter())

# 配置日志记录
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.StreamHandler(),  # 输出到控制台
        rotating_handler,
        # timed_rotating_handler, # 日志处理器同一个多个会出现重复写入log
        # smtp_handler
        MPFileLogHandler('one_file_log_2.log')
    ]
)
# 运行测试


from package_a import module_a1
# from package_b import module_b1
# from package_a import module_a2
from package_b.module_b2 import process_log
from multiprocessing import Pool
def run():
    p = Pool(4)
    for i in range(4):
        p.apply_async(process_log, args=(i,))
    print('waiting.....')
    p.close()
    p.join()
    print('done.....')

    
def main():
    logger = logging.getLogger(__name__)
    logger.info("主程序开始运行")
    run()
    module_a1.function_a1()
    # module_a2.function_a2()
    # module_b1.function_b1()
    # module_b2.function_b2()

    logger.info("主程序结束运行")

if __name__ == "__main__":
    main()
