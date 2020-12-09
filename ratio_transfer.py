#分辨率对应屏幕比例计算
TEST_SCREENS = [(1920,1080),(1680,1050),(1600,1200),(1600,900), 
				(1280,960),(1280,800),(1280,768),(1280,720),(1280,600),
				(1152,864),(1024,768),(800,600)]
RATIO_TYPE1 = (16,9)
RATIO_TYPE2 = (4,3)

class Screen(object):
	"""屏幕尺寸信息"""
	def __init__(self, length, width):
		
		self.length = length
		self.width = width
		
"""
def testRatio(screenObject):
	if screenObject.length/RATIO_TYPE1[0] == screenObject.width/RATIO_TYPE1[1]:
		return RATIO_TYPE1
	elif screenObject.length/RATIO_TYPE2[0] == screenObject.width/RATIO_TYPE2[1]:
		return RATIO_TYPE2
	else:
		raise Exception(ValueError)

# TestScreen1 = Screen(1600,900)
# print(testRatio(TestScreen1))
# >> (16, 9)
"""

def getRatio(screenObject):
	#计算屏幕比例
	length = screenObject.length
	width = screenObject.width
	div_list = [num for num in range(1,width) if length%num==0 and width%num==0]
	"""for num in range(1,width):
		if not (length % num and width % num):
			pass"""
	max_num = max(div_list)
	#print(div_list)
	return (length/max_num, width/max_num)

"""
# 以下为 getRatio计算几个组合的结果
# print(getRatio(TestScreen1))
# >> (16.0, 9.0)
# print(getRatio(Screen(1440,900)))
# >> (8.0, 5.0)
# print(getRatio(Screen(1280,720)))
# >> (16.0, 9.0)
"""

def isTargetRatio(target):
	#列出所有符合目标要求比例的分辨率组合
	print([screen for screen in TEST_SCREENS 
			if getRatio(Screen(screen[0],screen[1])) == target])
	"""
		for screen in TEST_SCREENS:
		ratios = []
		ratio = getRatio(Screen(screen[0],screen[1]))
		ratios.append(ratio)
	"""

"""
# 以下为 RATIO_TYPE1与 RATIO_TYPE2测试结果
# isTargetRatio(RATIO_TYPE1)
# >> [(1920, 1080), (1600, 900), (1280, 720)]
# isTargetRatio(RATIO_TYPE2)
# >> [(1600, 1200), (1280, 960), (1152, 864), (1024, 768), (800, 600)]
"""
