import requests
import app
from utils.logger_get import LoggerGet

log = LoggerGet.get_logger()


# 定义封装登录接口
class LoginAPI:

    def __init__(self):
        self.url = app.LOGIN_URL

    # 定义登录接口方法
    def login(self, login_data):
        log.info("正在调用登录接口，url:{}，data:{}".format(self.url, login_data))
        return requests.post(self.url, json=login_data)
