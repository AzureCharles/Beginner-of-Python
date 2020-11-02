import random as rd
import time

#Gacha emulator from Arknights
"""
    Key points of card pool design:
     ①Support multiple sets of prize number imported from outside
     ②Support weighted probability output
     ③Support set-accessible probability
     ④Support built-in guarantee prize


    @prizeDict:卡池字典，包含卡池主要信息：prize，weight，probability
    @
"""
#


gachaResultDict = {}


class GachaPool():
    def __init__(self,pool_cap=100,):
        self.pool_capacity = pool_cap
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
