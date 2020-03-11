# -*-coding:utf-8-*-

import re


reObj = re.compile(r"[0-9]+-[0-9]+")

#计算平均工资
def saleAvg(msg):
    reResult = reObj.match(msg[1])
    if reResult != None:
        priceResult = re.split(r'\D', reResult.group(0))
        intPrice = [int(x) for x in priceResult]
        msg[1] = sum(intPrice) / len(intPrice)
#提取工作年限
def jodExperience(msg):
    reResult = reObj.findall(msg[4])

    if len(reResult) < 1:
        index1 = msg[4].find("经验不限")
        index2 = msg[4].find("应届生")
        index3 = msg[4].find("1年以内")
        if index1 > 0:
            msg[8] = msg[4][index1:index1 + 4]
        elif index2 > 0:
            msg[8] = msg[4][index2:index2 + 3]
        elif index3 > 0:
            msg[8] = msg[4][index3:index3 + 4]
    else:
        msg[8] = reResult[0]
#提取学历
def Education(msg):

    try:
        if len(msg[4]) > 2:
            msg[9] = msg[4][-2:]

    except Exception as e:

        print(msg)
        print(repr(e))

def addAddress(msg):

    if msg[3].find("区") == -1:
        msg.insert(3,"深圳市")






