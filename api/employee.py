import requests
import app
from utils.logger_get import LoggerGet

log = LoggerGet.get_logger()


class EmployeeAPI:

    def __init__(self):
        self.employee_add_url = app.EMPLOYEE_ADD
        self.employee_else_url = app.EMPLOYEE_ELSE

    # 员工添加
    def employee_add(self, add_data):
        log.info("正在调用员工添加接口，url：{}，add_data：{}，headers_data：{}".format(self.employee_add_url, add_data, app.headers_data))
        return requests.post(self.employee_add_url, json=add_data, headers=app.headers_data)

    # 员工修改
    def employee_update(self, update_data, employee_id):
        url = self.employee_else_url.format(employee_id)
        log.info("正在调用员工修改接口，url：{}，update_data：{}，headers_data：{}，employee_id：{}".format(url, update_data, app.headers_data, employee_id))
        return requests.put(url, json=update_data, headers=app.headers_data)

    # 员工查询
    def employee_get(self, employee_id):
        url = self.employee_else_url.format(employee_id)
        log.info("正在调用员工查询接口，url：{}，headers_data：{}，employee_id：{}".format(url, app.headers_data, employee_id))
        return requests.get(url, headers=app.headers_data)

    # 员工删除
    def employee_delete(self, employee_id):
        url = self.employee_else_url.format(employee_id)
        log.info("正在调用员工删除接口，url：{}，headers_data：{}，employee_id：{}".format(url, app.headers_data, employee_id))
        return requests.delete(url, headers=app.headers_data)
