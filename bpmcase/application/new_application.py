"""
手工新增
"""
import sys

from pages.projectPage import edit
import unittest


class projectGuide(unittest.TestCase):
    PG = edit()

    @classmethod
    def setUpClass(cls) -> None:
        cls.PG.login(account='014001-03')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.PG.driver.quit()

    def setUp(self) -> None:
        # self.PG.refresh()
        pass

    def tearDown(self) -> None:
        pass

    def test_01_approval(self):
        """教委新增项目审批通过"""
        self.PG.menuProject()
        self.PG.addProject()
        projectName = self.PG.edit(self._testMethodDoc)
        self.PG.projectSubmit()
        self.PG.lookView()
        nextUser = self.PG.findNextUserProject(1)
        self.PG.assertInText("待工作小组")
        self.PG.logout()
        self.PG.login2(nextUser)
        self.PG.menuProject()
        self.PG.listToView("待工作小组")
        self.PG.workGroupApprove()
        self.PG.menuProject()
        self.PG.listToView("待排序")
        log = self.PG.logBureau(projectName)
        log.info(str(self._testMethodDoc)+"操作成功，项目指南名称为："+projectName)
        self.PG.photo(folderName='guide', fileName=self._testMethodDoc)


if __name__ == "__main__":
    unittest.main()


