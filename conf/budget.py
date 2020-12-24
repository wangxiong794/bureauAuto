# coding=utf-8
"""绩效通生成预算模板接口自动化"""
import json

import requests
# 58.118.2.63

def item():
    # 按明细生成
    url = "http://jxt.neikongyi.com/bureau/service/interconnect/exportJbzcBudgetTemplate"

    data1 = {
        'budgetCode': "014704",
        'endDate': "2021-12-31T15:59:59.000Z",
        'hkCode': "g+WI6CmUPR729N+3c2RzdByUYFa3lzHNzP8k3EgtQ19L6H7B6M1bd70Lzm7IYxOVQAilnyTxrznpRi4IKegCRChsauDuEuo2cQF9dHfdK8hlS/0r/I2rn5rqn7t8Lz9DB9CSETrPjLkbjVXLh5qRiESq66BpXZ4nJX4Rxsy3VcY=",
        'isGroup': 0,
        'yearId': 10100,
    }
    headers1 = {
        "Content-Type": "application/json; charset=utf-8",
        "hkCode": "g+WI6CmUPR729N+3c2RzdByUYFa3lzHNzP8k3EgtQ19L6H7B6M1bd70Lzm7IYxOVQAilnyTxrznpRi4IKegCRChsauDuEuo2cQF9dHfdK8hlS/0r/I2rn5rqn7t8Lz9DB9CSETrPjLkbjVXLh5qRiESq66BpXZ4nJX4Rxsy3VcY="
    }
    a = requests.request('POST', url, data=json.dumps(data1), headers=headers1)
    text1 = str(a.text)
    print(a)
    print(text1,type(text1))

item()