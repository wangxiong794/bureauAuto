import sys

from bpmservice.special.allocation import edit
import unittest


class allocateGuide(unittest.TestCase):
    AT = edit()
    className = str(sys._getframe().f_code.co_name)

    @classmethod
    def setUpClass(cls) -> None:
        cls.AT.login(account='014001-03')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.AT.driver.quit()

    def setUp(self) -> None:
        # self.PG.refresh()
        pass

    def tearDown(self) -> None:
        pass

    def test_01_approval(self):
        """教委新增分配方案审批通过"""
        self.AT.menuAllocation()
        self.AT.add()
        allocationName = self.AT.edit(self._testMethodDoc)
        self.AT.submitAllocation()
        self.AT.lookView()
        nextUser = self.AT.findNextUserAllocation(1)
        self.AT.assertInText("待工作小组审核")
        self.AT.logout()
        self.AT.login2(nextUser)
        self.AT.menuAllocation()
        self.AT.listToView("待工作小组审核")
        self.AT.workGroupApprove()
        self.AT.menuAllocation()
        self.AT.listToView("待办公室复核")
        officeUser = self.AT.findNextUserAllocation(2)
        self.AT.logout()
        self.AT.login2(officeUser)
        self.AT.menuAllocation()
        self.AT.listToView("待办公室复核")
        self.AT.agree("办公室同意")
        self.AT.menuAllocation()
        self.AT.listToView()
        self.AT.assertNotInText("待审批")
        log = self.AT.logBureau(allocationName)
        log.info(str(self._testMethodDoc) + "操作成功，分配方案名称为：" + allocationName)
        self.AT.photo(folderName='guide', fileName=self._testMethodDoc)


if __name__ == "__main__":
    unittest.main()
