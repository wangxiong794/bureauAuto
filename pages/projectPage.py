# encoding: utf-8

"""
专项申报-项目库
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bpmservice.bpmcom import con
from common.readConfig import confParam
from common.GetElement import getElement


class homePage(con):
    iniFile = "projectElement.ini"
    section = 'edit'

    def _eleXpath(self, editPath):
        return self.eleXpath(self.section, editPath, self.iniFile)

    def findNextUserProject(self, suggestId, billType="project"):
        return self.findNextUser(suggestId, billType)

    def menuProject(self):
        self.choice_menu("专项申报","项目库")

    def addProject(self):
        time.sleep(0.5)
        self.buttonName("申报项目").click()
        self._eleXpath('choiceGuide').click()
        time.sleep(0.5)
        self._eleXpath('nextButton').click()
        time.sleep(0.5)
        self._eleXpath('nextButtonRead').click()

    def projectName(self,projectName="自动方案"):
        projectName = projectName + str(time.strftime("%Y-%m-%d %H:%M:%S"))
        self._eleXpath('projectName').send_keys(projectName)
        return projectName

    def projectClass(self):
        self._eleXpath("mainClass").click()
        time.sleep(0.1)
        self._eleXpath("mainClassInput").send_keys(Keys.ENTER)

    def projectIsNewSchool(self):
        self._eleXpath("isNewSchool").click()
        time.sleep(0.1)
        self._eleXpath("isNewSchoolInput").send_keys(Keys.ENTER)

    def projectPhone(self, phoneNumber='123456789145'):
        self._eleXpath("phone").send_keys(phoneNumber)

    def projectAmount(self,declareAmount='10000'):
        self._eleXpath("amount").send_keys(declareAmount)

    def projectDepartment(self):
        self._eleXpath("department").click()
        time.sleep(0.1)
        self._eleXpath("departmentInput").send_keys(Keys.ENTER)

    def projectTarget(self,targetName='1'):
        self._eleXpath("target").click()
        time.sleep(0.1)
        self._eleXpath("targetInput").send_keys(targetName)

    # 用款计划
    def usePlan(self, planName="测试", planDescription="测试", planDay='1', planAmount='10000'):
        self._eleXpath("usePlanName").click()
        time.sleep(0.1)
        self._eleXpath("usePlanNameInput").send_keys(planName)
        self._eleXpath("usePlanDescription").click()
        time.sleep(0.1)
        self._eleXpath("usePlanDescriptionInput").send_keys(planDescription)
        self._eleXpath("usePlanDay").click()
        time.sleep(0.1)
        self._eleXpath("usePlanDayInput").send_keys(planDay)
        self._eleXpath("usePlanAmount").click()
        time.sleep(0.1)
        self._eleXpath("usePlanAmountInput").send_keys(planAmount)

    def outPlan(self,planName="测试",planAmount="10000",planRemark="测试"):      # 支付明细
        self._eleXpath("outPlanName").click()
        time.sleep(0.1)
        self._eleXpath("outPlanNameInput").send_keys(planName)
        self._eleXpath("outPlanMethod").click()
        time.sleep(0.1)
        self._eleXpath("outPlanMethodInput").click()
        self._eleXpath("outPlanAmount").click()
        time.sleep(0.1)
        self._eleXpath("outPlanAmountInput").send_keys(planAmount)
        self._eleXpath("outPlanRemark").click()
        time.sleep(0.1)
        self._eleXpath("outPlanRemarkInput").send_keys(planRemark)

    def projectSubmit(self):
        self._eleXpath("projectSubmit").click()


class edit(homePage):
    def edit(self,projectName="自动测试", projectAmount="10000"):
        projectName = self.projectName(projectName)
        self.projectClass()
        self.projectPhone()
        self.projectIsNewSchool()
        self.projectAmount(projectAmount)
        self.projectDepartment()
        self.scrollBar(y=10000)
        self.projectTarget()
        self.usePlan(planAmount=projectAmount)
        self.outPlan(planName=projectAmount)
        return projectName


if __name__ == "__main__":
    c = edit()
    c.login('014001-03')
    c.menuProject()
    c.addProject()
    c.edit()
    c.quit()

