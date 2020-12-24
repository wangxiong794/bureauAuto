import sys

from bpmservice.special.projectguide import edit
import unittest
from selenium import webdriver


class projectGuide(unittest.TestCase):
    PG = edit()
    className = str(sys._getframe().f_code.co_name)

    @classmethod
    def setUpClass(cls) -> None:
        cls.PG.login(account='gwb')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.PG.driver.quit()

    def setUp(self) -> None:
        # self.PG.refresh()
        pass

    def tearDown(self) -> None:
        pass

    def test_01_approval(self):
        """新增项目指南审批通过并发布成功"""
        self.PG.menu()
        self.PG.add()
        guideName = self.PG.edit(self._testMethodDoc)
        self.PG.submit()
        self.PG.lookView()
        nextUser = self.PG.findNextUser(1)
        self.PG.assertInText("待分配专家")
        self.PG.logout()
        self.PG.login(nextUser)
        self.PG.menu()
        self.PG.listToView("待分配专家")
        self.PG.expertsGuide()
        self.PG.menu()
        self.PG.listToView("待专家论证")
        mainUser = self.PG.findNextUser(4)
        self.PG.logout()
        self.PG.login(mainUser)
        self.PG.menu()
        self.PG.listToView("待专家论证")
        viceUser1 = self.PG.findNextUser(3)
        self.PG.writeComments("主审审批")
        self.PG.logout()
        self.PG.login(viceUser1)
        self.PG.menu()
        self.PG.listToView("待专家论证")
        viceUser2 = self.PG.findNextUser(2)
        self.PG.writeComments("陪审1审批")
        self.PG.logout()
        self.PG.login(viceUser2)
        self.PG.menu()
        self.PG.listToView("待专家论证")
        self.PG.writeComments("陪审2审批")
        self.PG.logout()
        self.PG.login(nextUser)
        self.PG.menu()
        self.PG.listToView("待专家复核")
        self.PG.agree()
        self.PG.menu()
        self.PG.listToView("待报领导小组")
        leadUser = self.PG.findNextUser(6)
        self.PG.logout()
        self.PG.login(leadUser)
        self.PG.menu()
        self.PG.listToView("待报领导小组")
        self.PG.reportGroup()
        self.PG.menu()
        self.PG.listToView("待领导小组批复")
        groupUser = self.PG.findNextUser(7)
        self.PG.logout()
        self.PG.login(groupUser)
        self.PG.menu()
        self.PG.listToView("待领导小组批复")
        self.PG.agree("领导小组同意")
        self.PG.menu()
        self.PG.listToView("待区长批复")
        bossUser = self.PG.findNextUser(8)
        self.PG.logout()
        self.PG.login(bossUser)
        self.PG.menu()
        self.PG.listToView("待区长批复")
        self.PG.agree("区长同意")
        self.PG.menu()
        self.PG.listToView()
        self.PG.assertNotInText("待审批")
        self.PG.publish()
        log = self.PG.logBureau(guideName)
        log.info(str(self._testMethodDoc)+"操作成功，项目指南名称为："+guideName)
        self.PG.photo(folderName='guide', fileName=self._testMethodDoc)


if __name__ == "__main__":
    # a = projectGuide()
    # a.setUpClass()
    # a.setUp()
    # a.test_1()
    # a.tearDownClass()
    unittest.main()


