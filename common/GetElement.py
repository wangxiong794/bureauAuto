# encoding: utf-8

import time

from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os
from selenium import webdriver
from getRootPath import root_dir


class getElement:
    def __init__(self, elementFile):
        self.elementPath = os.path.join(root_dir, "elements")
        self.elementIni = os.path.join(self.elementPath, elementFile)

    def getElement(self, driver, section, option):
        try:
            f = configparser.ConfigParser()
            f.read(self.elementIni,encoding='utf-8')  # 读配置文件内容到内存中
            locators = f.get(section, option).split(':')
            # 获取定位方式
            locMethod = locators[0]
            # 获取定位表达式
            locExpression = locators[1]
            # 通过显示等待的方式获取页面的元素
            element = WebDriverWait(driver, 5).until(lambda x: x.find_element(locMethod, locExpression), message="定位超时")
        except Exception as e:
            raise e
        else:
            return element


if __name__ == '__main__':
    ele = getElement("loginPageElement.ini")
    driver = webdriver.Chrome()
    driver.get('http://jxt.neikongyi.com/bureau')
    element1 = ele.getElement(driver, 'login', 'account')
    element1.send_keys('18042477732')
    element1 = ele.getElement(driver, 'login', 'password')
    print(element1,type(element1))
    element1.send_keys('syy0107!@#$')
    time.sleep(2)
    driver.quit()
