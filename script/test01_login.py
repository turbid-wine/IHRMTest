# 导包
import app
import unittest
from api.login import LoginAPI
from utils.common_assert import common_assert
from utils.logger_get import LoggerGet

log = LoggerGet.get_logger()


# 创建测试类
class TestLogin(unittest.TestCase):
    # 前置处理
    def setUp(self):
        log.info("正在初始化TestLogin测试类")
        self.login_api = LoginAPI()

    # 定义测试用例
    # case001 登录成功
    def test01_case001(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, True, 10000, "操作成功")

        # # 提取token信息
        # app.TOKEN = "Bearer " + response.json().get("data")
        # print(app.TOKEN)
        # app.headers_data["Authorization"] = app.TOKEN
        # print(app.headers_data["Authorization"])

    # case002 不输入手机号
    def test02_case002(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "", "password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case003 不输入密码
    def test03_case003(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002", "password": ""})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case004 手机长度小于11位
    def test04_case004(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "1380000000", "password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case005 手机场地大于11位
    def test05_case005(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "138000000023", "password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case006 手机号输入非数字
    def test06_case006(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "error", "password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case007 输入未注册手机号
    def test07_case007(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13812321236", "password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case008 多参
    def test08_case008(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "haha": "xixi"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, True, 10000, "操作成功")

    # case009 少参-缺少手机号
    def test09_case009(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case010 少参-缺少密码
    def test10_case010(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case011 无参
    def test11_case011(self):
        # 调用登录接口进行登录
        response = self.login_api.login(None)
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 99999, "抱歉，系统繁忙")

    # case012 错误参数-手机号
    def test12_case012(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobiel": "13800000002", "password": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # case013 错误参数-密码
    def test13_case013(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002", "passwd": "123456"})
        print(response.json())

        # 断言
        common_assert(self, response, 200, False, 20001, "用户名或密码错误")