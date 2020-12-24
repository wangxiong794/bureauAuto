# coding=utf-8
"""

"""
import unittest

import time
from selenium import webdriver

from common.readConfig import confParam
from pages.loginPage import LoginPage
from ddt import ddt, data
from getRootPath import root_dir
import os
from common.readYaml import operYaml
from common.writeLog import writeLog
from common.screen import getScreen



@ddt
class test_登录(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yamlCase", "登录.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()


    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = webdriver.Chrome()

    # case_list传进去做数据驱动
    @data(*case_list)
    def test_登录(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            account = caseInfo["account"]
            password = caseInfo["password"]
            check = caseInfo["assert"]
            self.__dict__['_testMethodDoc'] = caseName

        driver = self.driver
        url = confParam("url")
        login_Page = LoginPage(driver, url)

        # 打开首页
        login_Page.open_home_page()
        # 输入账号
        login_Page.input_userName(account)
        # 输入密码
        login_Page.input_passwd(password)

        # 点击登录
        login_Page.click_login_btn()

        # 断言
        time.sleep(3)
        getScreen(self.driver, caseName, "login")
        self.assertIn(check, self.driver.page_source)
        # 写日志文件
        case_info = {"用例名字: ": caseName, "登录账号:": account, "密码: ": password, "断言：": check}
        writeLog(case_info)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()