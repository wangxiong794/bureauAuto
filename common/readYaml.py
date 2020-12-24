# coding=utf-8


import yaml
import os
from getRootPath import root_dir


class operYaml:
	def __init__(self, yamlPath):
		self.yamlPath = yamlPath

	def caseList(self):
		with open(self.yamlPath, 'r', encoding='utf-8') as fp:
			contents = fp.read()
			testCase_dict = yaml.safe_load(contents)
			case_list = []
			for caseName, caseInfo in testCase_dict.items():
				new_dict = {}
				new_dict[caseName] = caseInfo
				case_list.append(new_dict)
			return case_list


if __name__ == "__main__":
	yamlPath = os.path.join(root_dir, "yamlCase", "登录.yaml")
	oper_yaml = operYaml(yamlPath)
	case_list = oper_yaml.caseList()
	for i in case_list:
		print(i)
