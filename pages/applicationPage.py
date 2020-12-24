"""
预算申请-项目预算申请
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bpmservice.bpmcom import con


class homePage(con):
    iniFile = "BaElement.ini"
    section = 'edit'

    def _eleXpath(self, editPath, _section=section, _infile=iniFile):
        return self.eleXpath(_section, editPath, _infile)

    def findNextUserProject(self, suggestId, billType="project"):
        return self.findNextUser(suggestId, billType)

    def menuApplication(self):
        # self.choice_menu("预算申请", "项目预算申请")
        self._eleXpath(editPath='menu1', _section='menu').click()
        self.untilFindText('项目预算申请')
        self._eleXpath(editPath='menu2',_section='menu').click()

    def baList(self):  # 选预算申请单卡片
        self.untilFindText('预算申请单')
        self._eleXpath(editPath='baList', _section='list').click()

    def addNewBa(self):
        time.sleep(0.5)
        self._eleXpath(editPath='startNewBaButton', _section='list').click()

    def baType(self):  # 预算类型
        self.untilFindText('baBudgetTypeId')
        self._eleXpath('baType').click()
        self.untilFindText('纳入部门预算')
        self._eleXpath('baTypeInput').send_keys(Keys.ENTER)

    def baAmountSource(self):  # 资金来源
        self._eleXpath('baAmountSource').click()
        self.untilFindText('追加预算')
        self._eleXpath('baAmountSourceInput').send_keys(Keys.ENTER)

    def baName(self, _projectName="手工新增预算单"):
        self._eleXpath('baName').send_keys(_projectName)

    def baProjectType(self):    # 项目类型
        self._eleXpath('baProjectType').click()
        self.untilFindText('业务性专项')
        self._eleXpath('baProjectTypeInput').send_keys(Keys.ENTER)

    def startProjectDate(self):     # 项目申报时间
        self._eleXpath('startProjectDate').click()
        self.untilFindText('今天')
        self._eleXpath('startProjectDateEnter').click()

    def baEducationClass(self):     # 教育资金类别
        self._eleXpath('baEducationClass').click()
        self.untilFindText('义务教育均衡发展')
        self._eleXpath('baEducationClassInput').send_keys(Keys.ENTER)

    def nbAmount(self,_nbAmount='1000'):     # 拟拨资金
        self._eleXpath('nbAmount').send_keys(_nbAmount)

    def bcAmount(self,_bcAmount='1000'):       # 本次申请金额
        self._eleXpath('bcAmount').send_keys(_bcAmount)

    def baAllocateLot(self):    # 拨款批次
        self._eleXpath('baAllocateLot').click()
        self._eleXpath('baAllocateLotInput').send_keys(Keys.ENTER)

    def projectName(self,_projectName='test'):      # 项目预算名称
        self._eleXpath('projectName').click()
        self._eleXpath('projectNameInput').send_keys(_projectName)

    def functionName(self):
        ele = self._eleXpath('functionName')
        self.untilFindText('227 预备费')
        ActionChains(self.driver).move_to_element(ele).click(ele).send_keys(Keys.ENTER).perform()


class edit(homePage):
    def edit(self):
        self.baType()
        self.baAmountSource()
        self.baName()
        self.baProjectType()
        self.startProjectDate()
        self.baEducationClass()
        self.nbAmount()
        self.bcAmount()

    def projectItem(self):  # 项目预算明细
        self.scrollBar()
        self.projectName()
        self.functionName()

if __name__ == "__main__":
    c = edit()
    c.login('014999001')
    c.menuApplication()
    c.baList()
    c.addNewBa()
    c.edit()
    c.projectItem()