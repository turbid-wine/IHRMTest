import time
import unittest
from utils.HTMLTestRunner import HTMLTestRunner


# 定义测试套件，执行script文件中test（默认按序号执行）
suit = unittest.defaultTestLoader.discover("./script")
# 定义报告生成目录
report_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 获取文件流并执行run
with open(report_path, "wb") as f:
    HTMLTestRunner(stream=f, title="IHRM自动化测试报告", description="win10操作系统").run(suit)
