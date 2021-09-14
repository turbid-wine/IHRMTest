import unittest
import app
from api.login import LoginAPI
from parameterized import parameterized
from utils.read_json import read_json
from utils.logger_get import LoggerGet

log = LoggerGet.get_logger()


# 参数化测试数据
def build_data():
    json_file = "./data/login.json"
    dict_data = read_json(json_file)
    # 定义接收列表
    test_data = []

    for data in dict_data:
        login_data = data.get("login_data")
        status_code = data.get("status_code")
        success = data.get("success")
        code = data.get("code")
        message = data.get("message")
        test_data.append((login_data, status_code, success, code, message))
    log.info("正在执行数据驱动，data={}".format(test_data))
    return test_data


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
       log.info("正在初始化LoginTest测试类")
       self.login_api = LoginAPI()

    def tearDown(self) -> None:
        pass

    # 定义测试用例 - 登录成功，并且获取token
    def test_login01(self):
        log.info("正在执行test_login01测试方法")
        login_data = {
            "mobile": "13800000002",
            "password": "123456"
        }
        response = self.login_api.login(login_data)
        log.info("返回response：{}".format(response.text))

        try:
            # 断言
            self.assertEqual(200, response.status_code)     # 获取响应状态码
            self.assertEqual(True, response.json().get("success"))
            self.assertEqual(10000, response.json().get("code"))
            self.assertIn("操作成功", response.json().get("message"))
        except Exception as e:
            log.error("[test_login01]断言出错{}".format(e))

        app.TOKEN = response.json().get("data")
        app.headers_data["Authorization"] = app.TOKEN
        log.info("TOKEN获取成功，TOKEN = {}".format(app.TOKEN))

    @parameterized.expand(build_data)
    def test_login02(self, login_data, status, success, code, message):
        log.info("正在执行test_login02测试方法")
        # 调用登录接口
        response = self.login_api.login(login_data)
        log.info("返回response：{}".format(response.text))
        try:
            # 断言
            self.assertEqual(status, response.status_code)
            self.assertEqual(success, response.json().get("success"))
            self.assertEqual(code, response.json().get("code"))
            self.assertIn(message, response.json().get("message"))
        except Exception as e:
            log.error("[test_login02]断言出错{}".format(e))
