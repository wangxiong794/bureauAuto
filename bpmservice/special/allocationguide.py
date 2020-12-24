import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from bpmservice.bpmcom import con
from bpmservice.special.projectguide import guide


class allocateGuide(guide):
    def menuAllocate(self):
        self.choice_menu("专项申报", "方案指南")

    def typeAllocate(self):
        time.sleep(0.1)
        self.dr("//div[@id='projectTypeId']/div/div").click()
        time.sleep(0.1)
        self.inputId('projectTypeId').send_keys(Keys.ENTER)

    def guideTextAllocate(self):
        ele = self.dr(
            '//*[@id="globalLayoutContent"]/div/div/div[3]/div[2]/div/section[2]/div[1]/div/div/span/div/textarea')
        action = ActionChains(self.driver)
        action.move_to_element(ele).click(ele)
        action.send_keys("贯彻落实北京市和海淀区关于推进中小学集团化办学的有关精神，深入推进教育集团化办学模式改革，充分发挥品牌学校的辐射带动作用，激发学校办学活力，整体提升集团各成员校办学质量，进一步扩大全区优质教育资源覆盖面和受益面，促进教育优质均衡发展。\
        创新教育集团人事管理制度，加大对教育集团的经费支持力度，健全集团内部管理机制，支持教育集团扩大资源统筹利用，促进干部教师交流轮岗，深化人才联合培养和贯通培养。积极引导和支持教育集团有序发展，教育结构和布局更加合理，办学体制机制不断完善，政策支持和保障机制不断健全，现代学校制度初步建立，教育公共服务水平和能力全面提升。")
        action.send_keys(Keys.TAB).send_keys("项目经费由集团总校在集团校内按照“总额控制、集团内部调剂”的原则统筹支配使用。原则上集团总校主要用于智力支持、智力投入和外聘人员经费，被承办校可用于教育改革与发展专项方面的支出。\
        承办经费使用应符合相关管理规定，不得用于“三公”经费及基本建设支出。")
        action.send_keys(Keys.TAB).send_keys("项目经费支出应符合相关管理规定，集团总校的资金支出主要用于外聘人员经费，派出管理团队和学科教师、教科研指导与实践以及其他有助于教育教学质量提升的智力投入、智力支持等经费支出。\
        经费具体支出内容参照北京市教委、北京市财政局下发的《关于印发北京市城乡中小学校一体化发展项目管理办法的通知》精神，主要用于外聘人员经费、专家劳务费、咨询费、印刷费、培训费、材料费、市内交通补贴、差旅费等。\
        资金支出用于集团总校外聘人员经费的，须按照人事和财务相关规定执行。资金支出用于被承办校教育改革与发展专项方面的支出的，原则上控制在承办经费的30%以内。")
        action.send_keys(Keys.TAB).send_keys("在项目实施过程中，区教委改发办将联合相关科室和部门分别组织开展中期验收和终期验收，当年12月20日前项目结束时，要求各项目实施学校提交项目总结报告和项目自评表。\
        进一步细化验收标准，把集团组织机构调整与制度创新（如制定集团章程、发展规划等）、派出管理团队和骨干教师、课程共建共享、教师研修与培训、学生特色活动、教育设施资源共享、被承办校教育教学质量、家长学生满意度、社会认可度等具体指标纳入验收标准。\
        申报单位须提供项目实施的目标、具体工作概况、资金使用标准和范围、项目取得成果等；同时提供项目实施的过程性材料，如相关工作照片、视频、工作材料、工作成果等。").send_keys(Keys.TAB).perform()
        time.sleep(0.5)

    def dateAllocateGuide(self):    # 方案指南申报周期
        self.calendar2('applicationCycle')

    def unitAllocate(self):     # 方案指南选下属单位
        self.choiceUnit('014001')
        time.sleep(0.1)
        # self.choiceUnit('014002')
        # time.sleep(0.1)
        # self.choiceUnit('014999001')
        # time.sleep(0.1)
        self.buttonName("确 认").click()
        self.dr('//td[@id="0_personnelQuota"]/div').click()
        time.sleep(0.1)
        self.dr('//td[@id="0_personnelQuota"]/div/div/div/div[2]/input').send_keys("10000")
        self.dr("//td[@id='0_totalQuota']/div").click()
        time.sleep(0.1)
        self.dr("//td[@id='0_totalQuota']/div/div/div/div[2]/input").send_keys("20000")
    def submit(self):
        self.buttonName("提 交").click()


class edit(allocateGuide):
    def edit(self, guideName):
        guideName = self.guideName(guideName)
        self.typeAllocate()
        self.dateAllocateGuide()
        self.guideTextAllocate()
        self.unitAllocate()
        return guideName
