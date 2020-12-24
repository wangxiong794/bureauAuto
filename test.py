# coding=utf-8
import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class testA(object):
    def __init__(self, flag=0):
        if flag == 1:  # 为1时，不隐藏浏览器窗口
            self.driver = webdriver.Chrome(r"E:\eclipse\webdriver\chromedriver.exe")
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                           executable_path=r"E:\eclipse\webdriver\chromedriver.exe")
        self.dr = self.driver.find_element_by_xpath
        self.driver.implicitly_wait('30')
        self.driver.set_window_size('1360','800')

    def run(self, url="http://58.118.2.63/bureau",flag=1,user='cz'):
        self.driver.get(url)
        self.dr("//input[@id='userName']").send_keys(user)
        self.dr("//input[@id='password']").send_keys('nky2018')
        self.dr("//button[@data-test-id='LogInButton']").click()
        if flag == 0:
            self.dr("//div[text()='我的国拨']").click()
            time.sleep(0.3)
            self.dr(
                '//*[@id="globalLayoutContent"]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/div[2]/section/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]').click()
            self.dr('//button[text()="同意"]').click()
            self.dr("//textarea[@id='description']").send_keys('同意')
            self.dr("//span[text()='确 定']/..").click()
            log = Log()
            time.sleep(0.5)
            for i in range(0, 2000):
                try:
                    self.dr(
                        '//*[@id="globalLayoutContent"]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/div[2]/section/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]').click()
                    projectName = self.dr(
                        '//*[@id="globalLayoutContent"]/div/div[2]/div[2]/div[1]/section[1]/div[1]/div[2]').text
                    projectOrg = self.dr(
                        '//*[@id="globalLayoutContent"]/div/div[2]/div[2]/div[1]/section[1]/div[6]/div[2]').text
                    log.info("%s 的国拨项目： %s " % (projectOrg, projectName))
                    self.dr('//button[text()="同意"]').click()
                    self.dr("//textarea[@id='description']").send_keys('同意')
                    time.sleep(0.1)
                    self.dr("//span[text()='确 定']/..").click()
                except Exception as e:
                    log.info("定位超时，正在重试")
                    self.driver.quit()
                    return testA().run()
        else:
            self.dr("//div[text()='我的预算']").click()
            self.dr('//*[@id="globalLayoutContent"]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/div[2]/section/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]').click()
            self.dr('//button[text()="同意"]').click()
            self.dr("//textarea[@id='description']").send_keys('同意')
            self.dr("//span[text()='确 定']/..").click()
            self.dr('//*[@id="root"]/div/div/nav/div[1]/ul/li[1]').click()
            self.dr('//*[@id="root"]/div/div/nav/div[1]/ul/li[1]/span[1]').click()
            self.dr('//*[@id="root"]/div/div/nav/div[1]/ul/li[1]').click()
            log = Log()
            time.sleep(0.5)
            for i in range(0, 2000):
                try:
                    self.dr(
                        '//*[@id="globalLayoutContent"]/div/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/div[2]/section/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]').click()
                    baCode = self.dr(
                        '//*[@id="globalLayoutContent"]/div[2]/div[1]/div[1]/div/div/span').text
                    orgCode = self.dr(
                        '//*[@id="globalLayoutContent"]/div[2]/div[2]/div[1]/section[1]/div[3]/div[2]').text
                    log.info("单位编码%s 的预算申请单： %s " % (orgCode, baCode))
                    self.dr('//button[text()="同意"]').click()
                    self.dr("//textarea[@id='description']").send_keys('同意')
                    time.sleep(0.1)
                    self.dr("//span[text()='确 定']/..").click()
                    time.sleep(0.3)
                    self.dr('//*[@id="root"]/div/div/nav/div[1]/ul/li[1]').click()
                    self.dr('//*[@id="root"]/div/div/nav/div[1]/ul/li[1]/span[1]').click()
                    self.dr('//*[@id="root"]/div/div/nav/div[1]/ul/li[1]').click()
                except Exception as e:
                    log.info("定位超时，正在重试")
                    self.driver.quit()
                    return testA().run()



class Log:
    def __init__(self):

        # 文件的命名
        self.logName = os.path.join(r".", '%s.log' % time.strftime('%Y_%m_%d'))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
    aa = testA()
    aa.run()
