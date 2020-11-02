import pandas as pd
import random as rd
import time

#Gacha emulator from Arknights
"""
    Key points of card pool design:
     ①Support multiple sets of prize number imported from outside
     ②Support weighted probability output
     ③Support set-accessible probability
     ④Support built-in guarantee prize

    关键字说明：
    @
    @
"""

class PrizesDict:   #卡池基本模板
    def __init__(self,ur_list,ssr_list,sr_list,r_list):
        prdict={}
        self.prdict['ur'] = ur_list
        self.prdict['ssr'] = ssr_list
        self.prdict['sr'] = sr_list
        self.prdict['r'] = r_list
    

prizeTotalDict = PrizesDict()

#尝试将这个字典直接封装为类型，可通过外部xls等文件导入

def selectPrize(prize_dict):
    pass
    prizeList = []  #记录卡池对象的元组列表
    printPrize(prizeList)
    return prizeList

def printPrize(prize_list):
    prize_keys = prizeTotalDict.key()
    for key in prize_keys:
        print(prize_keys[key]+": "+prize_list[key])

def getPoolContent(prizeList):
    prizeRates = [0.02,0.23,0.35,0.4]
    for index in prizeList:
        poolContent[prizeList[index]] = prizeRates[index]
    return poolContent

    #卡池列表初始化，key-value:编号-数量比例
    #为便于测试，



gachaResultDict = {}


class GachaPool:
    def __init__(self,poolContent,):
        self.pool = poolContent
        self.


def pool_initial(pool_capacity=100,prizeDict):
    gacha_pool = []
    gacha_pool.append(time.time())  #表首放置时间戳标识卡池序号
    for index in range(1,pool_capacity+1):
        gacha_pool.append(False)

    treasure = rd.randint(1,pool_capacity)
    gacha_pool[treasure] = True     #随机放置目标
    return gacha_pool

def gacha():
    #单次抽卡操作，结束后马上释放卡池并报告结果
    gacha_pool = pool_initial()
    gacha_result = gacha_pool[rd.randint(1,pool_capacity)]
    del gacha_pool
    return gacha_result

def gacha_congratulate(result_list):
    for result in result_list:
        if result:
            print("Congratulations!")
