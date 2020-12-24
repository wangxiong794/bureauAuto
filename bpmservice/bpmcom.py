import time
from unittest.util import safe_repr

from common import login, screen, readSetting, logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from common.GetElement import getElement


class con(object):
    """
        Page基类，所有page都应该继承该类
    """

    def __init__(self, interface=1):  # 如果不传driver，就默认这个值
        if interface == 1:
            self.driver = webdriver.Chrome(r"E:\eclipse\webdriver\chromedriver.exe")
            self.dr = self.driver.find_element_by_xpath
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
            self.dr = self.driver.find_element_by_xpath
        self.driver.implicitly_wait(15)
        self.driver.set_window_size(1366, 1000)

    def quit(self):
        self.driver.quit()

    def login(self, account):
        login.login(self.driver, account=account)

    def login2(self, userName, passWord="nky2018"):  # 非PO模式的登录
        self.dr("//input[@id='userName']").send_keys(userName)
        self.dr("//input[@id='password']").send_keys(passWord)
        self.buttonName("登 录").click()
        time.sleep(0.5)

    def photo(self, folderName, fileName):
        return screen.getScreen(self.driver, fileName, folderName)

    def choice_menu(self, menu1, menu2):
        time.sleep(0.5)
        # 鼠标hover至菜单
        ele = self.dr('//span[text()="' + menu1 + '"]/..')
        ActionChains(self.driver).move_to_element(ele).click(ele).move_to_element(ele).perform()
        ele.click()
        self.untilFindText("项目预算申请")
        try:
            time.sleep(0.5)
            self.dr("//a[text()='" + menu2 + "']").click()
        except:
            WebDriverWait(self.driver, 15).until(self.dr("//a[text()='" + menu2 + "']"), "菜单展开失败，请重试")
            self.driver.refresh()
            time.sleep(0.5)
            ActionChains(self.driver).move_to_element(ele).click(ele).move_to_element(ele).perform()
            ele.click()
            time.sleep(0.5)
            self.dr("//a[text()='" + menu2 + "']").click()

        time.sleep(0.5)

    def refresh(self):
        self.driver.refresh()
        time.sleep(1)

    def logout(self):
        self.driver.execute_script('document.querySelector("#globalLayoutContent").scrollTo(0,-10000)')
        time.sleep(0.1)
        self.dr("//*[@id='root']/div/div/div/div[1]/div/span[3]").click()
        time.sleep(0.01)
        self.dr("//li[text()='退出登录']").click()
        time.sleep(1)
        self.assertInText("登 录")

    def buttonName(self, buttonName):  # 通过span的中文定位
        return self.dr("//span[text()='" + buttonName + "']/..")

    def buttonNameReal(self, buttonName):
        return self.dr("//button[text()='" + buttonName + "']")

    def inputId(self, inputId="name"):  # 通过input的id定位
        return self.dr("//input[@id='" + inputId + "']")

    def li(self, liName):  # 通过li的中文定位
        return self.dr("//li[text()='" + liName + "']")

    def td(self, tdName):
        return self.dr("//td[text()='" + tdName + "']")

    def calendar2(self, calendarId='dateRange'):  # 日历 选择日期段
        self.dr("//span[@id='" + calendarId + "']/span/input[1]").click()
        time.sleep(0.5)
        self.dr("//td[contains(@class,'ant-calendar-today')]/div").click()
        time.sleep(1)
        self.dr("//td[contains(@class,'ant-calendar-today')]/div").click()

    def testAreaName(self, testAreaName):  # 通过testarea的placeholder定位
        return self.dr("//textarea[@placeholder='" + testAreaName + "']")

    def lookView(self):
        self.buttonName("查看详情").click()
        time.sleep(1)
        self.dr("//div[text()='审批意见']").click()
        time.sleep(0.2)

    def findNextUser(self, suggestId=0, billType="guide"):  # 查找下一审批人用户
        """suggestId 为审批意见中的第几条，为0时，则不查找下一审批人"""
        if billType == "guide":
            if suggestId == 0:
                pass
            else:
                self.driver.execute_script('document.querySelector("#globalLayoutContent").scrollTo(0,10000)')
                # userName = self.dr("//section/div[" + str(suggestId) + "]/div[1]/div[2]").text
                userName = self.dr('//*[@id="globalLayoutContent"]/div/div[4]/div/div/section[2]/div[' + str(suggestId)
                                   + ']/div[1]/div[2]').text
                userName = str(readSetting.readUser(str(userName)))
                log = logger.Log()
                if userName is None:
                    log.error("没找到用户登录名")
                else:
                    log.info("下一审批人" + userName)
                    return userName
        elif billType == "allocation":
            if suggestId == 0:
                pass
            else:
                self.driver.execute_script('document.querySelector("#globalLayoutContent").scrollTo(0,10000)')
                # userName = self.dr("//section/div[" + str(suggestId) + "]/div[1]/div[2]").text
                userName = self.dr('//*[@id="globalLayoutContent"]/div/div[4]/div/div/div/section[2]/div[' +
                                   str(suggestId) + ']/div[1]/div[2]').text
                userName = str(readSetting.readUser(str(userName)))
                log = logger.Log()
                if userName == "None":
                    log.error("没找到用户登录名")
                else:
                    log.info("下一审批人" + userName)
                    return userName
        elif billType == "project":
            if suggestId == 0:
                pass
            else:
                self.driver.execute_script('document.querySelector("#globalLayoutContent").scrollTo(0,10000)')
                # userName = self.dr("//section/div[" + str(suggestId) + "]/div[1]/div[2]").text
                userName = self.dr('//*[@id="globalLayoutContent"]/div/div/div[5]/div/div/div/section[2]/div[' +
                                   str(suggestId) + ']/div[1]/div[2]').text
                userName = str(readSetting.readUser(str(userName)))
                log = logger.Log()
                if userName == "None":
                    log.error("没找到用户登录名")
                else:
                    log.info("下一审批人" + userName)
                    return userName
        else:
            log = logger.Log()
            log.error(billType + "字段类型未找到")

    def assertInText(self, member):
        """Just like self.assertTrue(a not in b), but with a nicer default message."""
        time.sleep(0.5)
        container = self.driver.page_source
        if member not in container:
            # standardMsg = '%s 字段未在源码中找到，源码内容为 %s' % (member, container)
            standardMsg = '%s 字段没有在页面中找到' % (member)
            log = logger.Log()
            log.warning(standardMsg)
        else:
            pass

    def assertNotInText(self, member):
        container = self.driver.page_source
        if member in container:
            standardMsg = '%s 字段页面中找到' % (member)
            log = logger.Log()
            log.warning(standardMsg)
        else:
            pass

    def untilFindText(self,_words):
        """Find words in page html until found it"""
        _pageText = self.driver.page_source
        if _words not in _pageText:
            time.sleep(0.1)
            return self.untilFindText(_words)
        else:
            pass

    def agree(self, opinion="同意"):
        self.buttonNameReal("同意").click()
        time.sleep(0.5)
        self.dr("//textarea[@placeholder='请输入审批意见']").send_keys(opinion)
        self.buttonName("确 定").click()
        time.sleep(0.1)

    def logBureau(self, Name):
        self.assertInText(Name)
        return logger.Log()

    def scrollBar(self, x=0, y=1000):  # 滚动条
        js = 'var q =document.querySelector("#globalLayoutContent").scrollTo(' + str(x) + ',' + str(y) + ')'
        self.driver.execute_script(js)

    def listToView(self, billStatus=""):
        time.sleep(0.1)
        self.dr("//table/tbody/tr[1]/td[2]").click()
        time.sleep(0.1)
        self.dr("//div[text()='审批意见']").click()
        time.sleep(0.1)
        if billStatus == "":
            pass
        else:
            self.assertInText(billStatus)

    def workGroupApprove(self):
        self.buttonNameReal("同意").click()
        time.sleep(0.5)
        ele = "//div[text()='同意']/../../div"
        self.dr(ele + "[2]/form/div[1]/div/div/div[2]/div/span/div/label[1]/span[1]/input").click()
        self.dr(ele + "[2]/form/div[2]/div/div/div[2]/div/span/div/label[1]/span[1]/input").click()
        self.dr(ele + "[2]/form/div[3]/div/div/div[2]/div/span/div/label[1]/span[1]/input").click()
        self.dr(ele + "[2]/form/div[4]/div/div/div[2]/div/span/div/label[2]/span[1]/input").click()
        self.dr(ele + "[2]/form/div[5]/div[2]/div/div/div/span/textarea").send_keys("工作小组同意")
        self.dr(ele + "[3]/div/button[2]").click()  # 确定

    def eleXpath(self, section, option, fileName="projectElement.ini"):  # 选择定位配置文件
        ele = getElement(fileName)
        ElePath = ele.getElement(self.driver, section, option)
        # print(ElePath, type(ElePath))
        # ElePath = self.dr(str(ElePath))  # 此次只支持xpath
        return ElePath
