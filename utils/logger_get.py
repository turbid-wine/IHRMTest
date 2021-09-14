import logging.handlers
import time


# 封装获取logger对象
class LoggerGet:

    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志级别
            cls.logger.setLevel(logging.DEBUG)
            # 获取控制台、文件处理器
            sh = logging.StreamHandler()
            th = logging.handlers.TimedRotatingFileHandler("./log/{}.log".format(time.strftime("%Y-%m-%d")),
                                                      when="D", interval=1, backupCount=30, encoding="utf-8")
            # 格式器设置
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)

            # 将格式器添加到处理器
            sh.setFormatter(fmt)
            th.setFormatter(fmt)

            # 将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger
