import json

"""
    封装读取json文件
"""


def read_json(json_file):

    # 打开json文件
    with open(json_file, encoding="utf-8") as f:
        # 读取json数据，并转换dict类型
        dict_data = json.load(f)
        # print("dict_data:", dict_data)
    return dict_data


if __name__ == '__main__':
    dict_data = read_json("../data/login.json")
    # 定义接收列表
    test_data = []
    for data in dict_data:
        login_data = data.get("login_data")
        status_code = data.get("status_code")
        success = data.get("success")
        code = data.get("code")
        message = data.get("message")
        test_data.append((login_data, status_code, success, code, message))
    print("test_data:", test_data)
