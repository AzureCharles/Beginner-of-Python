"""这是2020年9月28日MATLAB课上关于狼抓兔子问题的Python解答。
Background：
    已知某兔子可能藏身于1~10号环形洞穴中，某狼首先搜索第一个洞穴但未搜索到，随即间隔一个洞穴（即第三个）搜索，但仍未找到。
    此后，狼每次增加一个洞穴的间隔搜索，以此类推。若兔子要避免被狼找到，该躲进哪个或哪些洞穴比较稳妥？

Algorithm:
    环形洞穴可参考环形队列的设计思想，多于一圈时，以路程除周长的余数表示位置。
    洞穴编号索引与逻辑基本一致，除10号洞穴以0表示。
    
关键字说明：
    @holes：洞穴状态列表，以True表示某洞穴可能有兔子，以False表示无兔子
    @attempts_num：用户指定的测试次数 #事实上，基于算法逻辑，本题的结果是确定的，与这一参数大小无关
    @end_flag：用以判断循环结束的计数器
    @loc：表示狼所在位置，以holes列表索引表示
    @pace：表示狼选择的搜索步长
    @print_possible_hole(holes)：本文件指定的兔子可能位置输出函数，参数为一个列表
    @possible_holes：函数内部列表型变量，存储兔子可能位置的列表
    
History:
    2020年9月29日12:34:21
"""
holes = []
for hole in range(1,11):
    holes.append(True)
    #假定每个洞兔子藏身概率均等
attempts_num = int(input("Key in the times you want to try:"))
    #获取测试次数
end_flag = 0
loc = 1     #狼初始位置
pace = 1    #初始步长

while end_flag < attempts_num:
    holes[loc] = False
    #查找失败
    pace += 1
    loc = (loc + pace)%10
    #重定位
    end_flag += 1

print(holes)
    #注意，列表索引自0开始，呈现结果与逻辑不同
def print_possible_hole(holes):     #此处及函数体内部的holes均为形参
    possible_holes = []
    for hole in range(1,10):
        if holes[hole]:
            possible_holes.append(hole)
    if holes[0]:
        possible_holes.append(hole[0])   #对10号（索引0）单独判断
    print(possible_holes)
    
print_possible_hole(holes)
