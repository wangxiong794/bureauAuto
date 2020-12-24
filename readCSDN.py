# coding=utf-8
import logging
import os
import time
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class readCSDN(object):
    def __init__(self, flag=0):
        if flag == 1:   # 为1时，不隐藏浏览器窗口
            self.driver = webdriver.Chrome(r"E:\eclipse\webdriver\chromedriver.exe")
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                           executable_path=r"E:\eclipse\webdriver\chromedriver.exe")
        self.dr = self.driver.find_element_by_xpath

    def _wait(self, _xpath):
        WebDriverWait(self.driver, 5).until(self.dr(_xpath), message="定位超时")

    def untilFindText(self, _words,a=0):
        """Find words in page html until found it"""
        _pageText = self.driver.page_source
        if _words not in _pageText:
            if a < 3:
                b = a +1
                time.sleep(0.1)
                return self.untilFindText(_words,b)
            else:
                pass
        else:
            pass

    def read(self, articleName="怎样判断一个人的技术能力和水平"):
        url = readCSDNUrl(articleName)
        try:
            self.driver.get(url)
            self.untilFindText(articleName)
            time.sleep(1)
            self.driver.refresh()
            self.untilFindText(articleName)
            time.sleep(1)
            readAmount = self.dr("//div[@class='bar-content']/span[2]").text
            self.driver.quit()
        except:
            readAmount = "读取文章【%s】阅读数超时！！！" % articleName
        return readAmount


def readIni(_flag='url', _name='homeUrl'):
    cf = configparser.ConfigParser()
    cf.read(filenames=r'readCSDN.ini', encoding="utf-8")
    return cf.get(_flag, _name)


def readCSDNUrl(_name):
    articleId = readIni('articleId', _name)
    articleUrl = readIni('url', 'articleUrl')
    articleUrl = str(articleUrl + articleId)
    return articleUrl


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


def run(_number=1):
    cf = configparser.ConfigParser()
    cf.read(filenames=r'readCSDN.ini', encoding="utf-8")
    options = cf.options('articleId')
    log = Log()
    log.info("=============第 %s 次============" % str(i))
    for _articleName in options:
        rc = readCSDN()
        _amount = rc.read(_articleName)
        log.info(_articleName + ":阅读数(%s)" % _amount)
        time.sleep(5)


if __name__ == "__main__":
    # print(readCSDNUrl('怎样判断一个人的技术能力和水平'))
    for i in range(1,100):
        run()
        time.sleep(5)