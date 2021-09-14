"""
    url路径配置
"""
BASE_URL = "http://ihrm-test.itheima.net"
# 登录
LOGIN_URL = BASE_URL + "/api/sys/login"
# 员工添加
EMPLOYEE_ADD = BASE_URL + "/api/sys/user"
# 员工修改、查询、删除
EMPLOYEE_ELSE = BASE_URL + "/api/sys/user/{}"


# token
TOKEN = None

# 请求头数据 dict
# "Authorization": "Bearer bcfc9d2e-a575-4240-9569-f5f860619f97"
headers_data = {
    "Content-Type": "Application/json"
}
