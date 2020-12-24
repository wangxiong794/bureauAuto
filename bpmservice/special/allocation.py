import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from bpmservice.bpmcom import con


class allocation(con):
    def menuAllocation(self):
        self.choice_menu("专项申报", "分配方案")

    def add(self):
        self.buttonName("新增方案").click()

    def choiceAllocationGuide(self):  # 选择方案指南
        self.dr('//*[@id="globalLayoutContent"]/div/div/div[2]/div[2]/div/div/div/div/div/div['
                '2]/div/div/table/tbody/tr[1]').click()
        time.sleep(0.1)
        self.dr('//*[@id="globalLayoutContent"]/div/div/div[2]/div[3]/div/button[2]').click()

    def allocationName(self, allocationName):
        time.sleep(0.1)
        allocationName = allocationName + str(time.strftime("%Y-%m-%d %H:%M:%S"))
        self.inputId().send_keys(allocationName)
        return allocationName

    def textAllocate(self):  # 分配方案文本
        ele = self.dr('//*[@id="globalLayoutContent"]/div/div/div[2]/div/div[2]/div[2]/div/section[2]/div['
                      '1]/div/div/span/div/textarea')
        action = ActionChains(self.driver)
        action.move_to_element(ele).click(ele)
        action.send_keys('指根据评估分析或经验，对潜在的或可能发生的突发事件的类别和影响程度而事先制定的应急处置方案').send_keys(Keys.TAB)
        action.send_keys('以行政指令为主，兼顾学校共同意愿，将一所名校和若干所学校组成学校共同体（名校集团）的办学体制。以名校为龙头，'
                         '在教育理念、学校管理、教育科研、信息技术、教育评价、校产管理等方面统一管理，实现管理、师资、设备等优质教育资源的共享').send_keys(Keys.TAB)
        action.send_keys('集团化办学模板').send_keys(Keys.TAB).perform()

    def userAmount(self, userAvg=2000, users=2):  # 人员经费
        self.dr("//td[@id='0_personAvg']/div").click()
        time.sleep(0.2)
        self.dr("//td[@id='0_personAvg']/div/div/div/div[2]/input").send_keys(userAvg)
        self.dr("//td[@id='0_personNumber']/div").click()
        time.sleep(0.2)
        self.dr("//td[@id='0_personNumber']/div/div/div/div[2]/input").send_keys(users)

        self.dr("//td[@id='1_personAvg']/div").click()
        time.sleep(0.2)
        self.dr("//td[@id='1_personAvg']/div/div/div/div[2]/input").send_keys(userAvg)
        self.dr("//td[@id='1_personNumber']/div").click()
        time.sleep(0.2)
        self.dr("//td[@id='1_personNumber']/div/div/div/div[2]/input").send_keys(users)

    def submitAllocation(self):
        self.buttonName("提 交").click()
        time.sleep(1)

    def choiceProjectGuide(self):
        self.scrollBar()
        self.dr('//td[@id="0_specialGuideId"]/div').click()
        time.sleep(0.5)
        ele = "//div[text()='指南列表']/../.."
        self.dr(ele + "/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span/label/span/input").click()
        time.sleep(0.1)
        self.dr(ele + "//div[3]/div/button[2]").click()
        time.sleep(0.5)
        ele1 = "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div[2]/div/section[2]/div/div/div[" \
               "2]/div/div/div/div/div[1]/div/table/tbody/tr"
        self.dr(ele1 + "/td[4]/div").click()
        time.sleep(0.2)
        self.dr(ele1 + "/td[4]/div/div/div/div[2]/input").send_keys(1000)
        self.dr(ele1 + "/td[5]/div").click()
        time.sleep(0.2)
        self.dr(ele1 + "/td[5]/div/div/div/div/div/div/div/input").send_keys(Keys.ENTER)

    def findNextUserAllocation(self, suggestId=0, billType="allocation"):
        return self.findNextUser(suggestId, billType)


class edit(allocation):
    def edit(self, allocationName='自动方案'):
        self.choiceAllocationGuide()
        allocationName = self.allocationName(allocationName)
        self.textAllocate()
        self.choiceProjectGuide()
        self.userAmount()
        return allocationName



