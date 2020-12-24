import sys

from bpmservice.special.allocationguide import edit
import unittest


class allocateGuide(unittest.TestCase):
    AG = edit()
    className = str(sys._getframe().f_code.co_name)

    @classmethod
    def setUpClass(cls) -> None:
        cls.AG.login(account='gwb')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.AG.driver.quit()

    def setUp(self) -> None:
        # self.PG.refresh()
        pass

    def tearDown(self) -> None:
        pass

    def test_01_approval(self):
        """新增方案指南审批通过并发布成功"""
        self.AG.menuAllocate()
        self.AG.add()
        guideName = self.AG.edit(self._testMethodDoc)
        self.AG.submit()
        self.AG.lookView()
        nextUser = self.AG.findNextUser(1)
        self.AG.assertInText("待分配专家")
        self.AG.logout()
        self.AG.login(nextUser)
        self.AG.menuAllocate()
        self.AG.listToView("待分配专家")
        self.AG.expertsGuide()
        self.AG.menuAllocate()
        self.AG.listToView("待专家论证")
        mainUser = self.AG.findNextUser(4)
        self.AG.logout()
        self.AG.login(mainUser)
        self.AG.menuAllocate()
        self.AG.listToView("待专家论证")
        viceUser1 = self.AG.findNextUser(3)
        self.AG.writeComments("主审审批")
        self.AG.logout()
        self.AG.login(viceUser1)
        self.AG.menuAllocate()
        self.AG.listToView("待专家论证")
        viceUser2 = self.AG.findNextUser(2)
        self.AG.writeComments("陪审1审批")
        self.AG.logout()
        self.AG.login(viceUser2)
        self.AG.menuAllocate()
        self.AG.listToView("待专家论证")
        self.AG.writeComments("陪审2审批")
        self.AG.logout()
        self.AG.login(nextUser)
        self.AG.menuAllocate()
        self.AG.listToView("待专家复核")
        self.AG.agree()
        self.AG.menuAllocate()
        self.AG.listToView("待报领导小组")
        leadUser = self.AG.findNextUser(6)
        self.AG.logout()
        self.AG.login(leadUser)
        self.AG.menuAllocate()
        self.AG.listToView("待报领导小组")
        self.AG.reportGroup()
        self.AG.menuAllocate()
        self.AG.listToView("待领导小组批复")
        groupUser = self.AG.findNextUser(7)
        self.AG.logout()
        self.AG.login(groupUser)
        self.AG.menuAllocate()
        self.AG.listToView("待领导小组批复")
        self.AG.agree("领导小组同意")
        self.AG.menuAllocate()
        self.AG.listToView("待区长批复")
        bossUser = self.AG.findNextUser(8)
        self.AG.logout()
        self.AG.login(bossUser)
        self.AG.menuAllocate()
        self.AG.listToView("待区长批复")
        self.AG.agree("区长同意")
        self.AG.menuAllocate()
        self.AG.listToView()
        self.AG.assertNotInText("待审批")
        self.AG.publish()
        log = self.AG.logBureau(guideName)
        log.info(str(self._testMethodDoc) + "操作成功，方案指南名称为：" + guideName)
        self.AG.photo(folderName='guide', fileName=self._testMethodDoc)


if __name__ == "__main__":
    unittest.main()