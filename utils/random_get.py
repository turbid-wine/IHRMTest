import random
import string


# 随机生成字符串
def get_str():
    # 从a-zA-Z0-9生成指定数量的随机字符
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    # print(ran_str)
    return ran_str


# 随机生成手机号
def get_phone():
    list_data = ['139', '138', '137', '136', '135', '134', '159', '158', '157']
    str_data = string.digits    # 0123456789
    for i in range(1):
        phone = random.choice(list_data) + "".join(random.choice(str_data) for i in range(8))
        # print(phone)
    return phone


# 随机生成9位数字
def get_number():
    ran_number = ''.join(random.sample(string.digits, 9))
    # print(ran_number)
    return ran_number


if __name__ == '__main__':
    # get_str()
    get_phone()
    # get_number()
