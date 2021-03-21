#Azurelane simple tools
"""
#This is a Georgia-Formidable coordinator based on the file:
    "可畏佐治亚调速计算器1.03.xlsx" from @玄虚小圣

#Developer's instructions(by @玄虚小圣):
    这个是用于给可畏-佐治亚这个组合调速用的（当然，其他战列也可以用，原理一样）
调速原理介绍：
    ·可畏的时停有1.5秒，我们需要佐治亚的超重弹在这1.5秒内击中目标。
    ·考虑到一般战斗有3~4轮主炮，所以可畏不能比佐治亚快（可畏先起飞会导致佐治亚吃不到时停）也不能慢太多
    （碰上大凤这种高移动力boss的话，时停结束后的减速效果比时停差很多）
    ·另外注意，战列炮还有0.3秒的抬手前摇。

#用法(by @玄虚小圣)：
    (1)首先，默认可畏第三格是+10的紫青花鱼，如果没这个鱼雷机的话，可畏废掉了自身输出，而且调速也麻烦
    (2)表格里输入佐治亚的面板CD（去舰船装备替换界面自己看）和可畏的面板装填（比如200好感是124）以及可畏受到的科技装填，和猫的装填（填入这两个的总和）
    (3)然后看下面的表格（分为带信标和不带信标两种），从里面找到符合调速区间的战/轰+鱼雷机组合

#以上内容引自 哔哩哔哩Wiki-碧蓝海事局：http://wiki.biligame.com/blhx，
    文字内容遵守【署名-非商业性使用-相同方式共享 3.0 (CC BY-NC-SA 3.0)】协议
#原文链接：
    https://wiki.biligame.com/blhx/%E5%8F%AF%E7%95%8F%E4%BD%90%E6%B2%BB%E4%BA%9A%E8%B0%83%E9%80%9F%E8%AE%A1%E7%AE%97%E5%99%A8
    
#Dictionary:
    short Formidable as @fmd
    
    @Twi457mmMKAT0: 双联装457mmMKAT0主炮，即二期科研六星彩炮、佐治亚炮；
    @Twi406mmSKCT0: 双联装406mmSKCT0主炮，即二期科研速射高爆、大帝炮；
    @Tri406mmMK6T3: 三联装406mmMK6T3主炮，即四星高爆白鹰炮、MK6；
    @Tri381mmT0:    三联装381mmT0主炮，即一期科研高爆、君主炮；
    @Tri410mmT0:    三联装410mmT0主炮，即一期科研穿甲、出云炮；
    @beacon:Homing beacon T0,归航信标T0；
"""
import numpy as np
import pandas as pd

GUN_SPEED = {'Twi457mmMKAT0':20.65, 'Twi406mmSKCT0':19.42, 
            'Tri406mmMK6T3':20.02,'Tri381mmT0':23.14,
            'Tri410mmT0':24.14}
            
AIRCRAFT_SPEED = {}
PI = 3.14

def getWeaponCd(gun_spd,tchc_ld=4,cat_ld=6,bsld_buff=0,bship_ld=173):
    #bship_ld:大炮装填数值，默认值是120级佐治亚200好感的装填173
    #bsld_buff:大炮装填buff
    ld_effcy = pow(200/((bship_ld+tchc_ld+cat_ld)*(1+bsld_buff)+100),0.5)
    mainGunCd = ld_effcy*gun_spd
    return mainGunCd
    #计算主炮装备面板
    

def getPlayerData(mg_cd,out_ld=0.08,tchc_ld=19,cat_ld=0,fmd_ld=124,):
    playerData = {}
    playerData['mainGun_cd'] = mg_cd
    playerData['Fmd_load'] = fmd_ld
    playerData['load_buff'] = out_ld
    playerData['tech_load'] = tech_ld
    playerData['cat_load'] = cat_ld
    return playerData

def getGunFireTime():
    pass
    
def inital_AircraftList():
    ca_dict = {}
