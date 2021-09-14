import app
from api.login import LoginAPI


# 登录成功，获取token  调试专用
def login_success():
    login_data = {
        "mobile": "13800000002",
        "password": "123456"
    }

    response = LoginAPI().login(login_data)
    print(response.json())

    app.TOKEN = response.json().get("data")
    print("TOKEN:", app.TOKEN)
    app.headers_data["Authorization"] = app.TOKEN
    print("app.headers_data:", app.headers_data.items())


if __name__ == '__main__':
    login_success()
