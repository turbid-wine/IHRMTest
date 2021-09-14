import unittest
from api.employee import EmployeeAPI
from utils.common_assert import common_assert
from utils.login_success import login_success
from utils import random_get
from utils.logger_get import LoggerGet

log = LoggerGet.get_logger()


class EmployeeTest(unittest.TestCase):

    # 定义员工ID全局变量
    employee_id = None

    def setUp(self) -> None:
        # login_success()
        log.info("正在初始化EmployeeTest测试类")
        self.employee_api = EmployeeAPI()

    # 员工添加
    def test01_add_employee(self):
        log.info("正在执行test01_add_employee测试方法")
        add_data = {
            "username": random_get.get_str(),
            "mobile": random_get.get_phone(),
            "timeOfEntry": "2021-07-26",
            "formOfEmployment": 1,
            "workNumber": random_get.get_number(),
            "departmentName": "自动化测试",
            "departmentId": "33660",
            "correctionTime": "2021-10-26"
        }
        response = self.employee_api.employee_add(add_data)
        log.info("返回response：{}".format(response.text))
        try:
            # 断言
            common_assert(self, response)
        except Exception as e:
            log.error("[test01_add_employee]断言出错{}".format(e))

        # 获取员工ID
        EmployeeTest.employee_id = response.json().get("data").get("id")
        log.info("员工添加成功，员工ID为{}".format(EmployeeTest.employee_id))

    # 员工修改
    def test02_update_employee(self):
        log.info("正在执行test02_update_employee测试方法")
        data = {
            "username": "jack111",
            "departmentName": "系统测试"
        }
        response = self.employee_api.employee_update(data, EmployeeTest.employee_id)
        log.info("返回response：{}".format(response.text))

        try:
            # 断言
            common_assert(self, response)
        except Exception as e:
            log.error("[test02_update_employee]断言出错{}".format(e))

    # 员工查询
    def test03_get_employee(self):
        log.info("正在执行test03_get_employee测试方法")
        response = self.employee_api.employee_get(EmployeeTest.employee_id)
        log.info("返回response：{}".format(response.text))
        try:
            # 断言
            common_assert(self, response)
        except Exception as e:
            log.error("[test02_update_employee]断言出错{}".format(e))

    # 员工删除
    def test04_delete_employee(self):
        log.info("正在执行test04_delete_employee测试方法")
        response = self.employee_api.employee_delete(EmployeeTest.employee_id)
        log.info("返回response：{}".format(response.text))
        try:
            # 断言
            common_assert(self, response)
        except Exception as e:
            log.error("[test02_update_employee]断言出错{}".format(e))
