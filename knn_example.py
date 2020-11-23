#  knn_example.py
#  
#  代码改编自：https://www.cnblogs.com/ahu-lichang/p/7151007.html
#  例子来自：https://blog.csdn.net/saltriver/article/details/52502253
#  
#!/usr/bin/python
# coding=utf-8
#########################################
# kNN: k Nearest Neighbors

#输入：  newInput:  (1xN)的待分类向量
#       dataSet:   (NxM)的训练数据集
#       labels:    训练数据集的类别标签向量
#            k:    近邻数

# 输出:     可能性最大的分类标签
#########################################

from numpy import *
import operator
import numpy as np

movie_data = {"宝贝当家": [45, 2, 9, "喜剧片"],
              "美人鱼": [21, 17, 5, "喜剧片"],
              "澳门风云3": [54, 9, 11, "喜剧片"],
              "功夫熊猫3": [39, 0, 31, "喜剧片"],
              "谍影重重": [5, 2, 57, "动作片"],
              "叶问3": [3, 2, 65, "动作片"],
              "伦敦陷落": [2, 3, 55, "动作片"],
              "我的特工爷爷": [6, 4, 21, "动作片"],
              "奔爱": [7, 46, 4, "爱情片"],
              "夜孔雀": [9, 39, 8, "爱情片"],
              "代理情人": [9, 38, 2, "爱情片"],
              "新步步惊心": [8, 34, 17, "爱情片"]}

#   测试电影A: [23, 3, 17, "喜剧片"]
#   测试电影B: [25, 27, 12, "爱情片"]



def createDataSet():
    group = array([attr[:3] for attr in movie_data.values()])
    #生成一个矩阵，每行表示一个样本
    labels = [attr[-1] for attr in movie_data.values()]
    #以电影类型为标签
    return group, labels
    #返回属性和对应标签

# KNN分类算法函数定义
def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]   # shape[0]表示行数

    # # step 1: 计算距离[
    # 假如：
    # Newinput：[1,0,2]
    # Dataset:
    # [1,0,1]
    # [2,1,3]
    # [1,0,2]
    # 计算过程即为：
    # 1、求差
    # [1,0,1]       [1,0,2]
    # [2,1,3]   --   [1,0,2]
    # [1,0,2]       [1,0,2]
    # =
    # [0,0,-1]
    # [1,1,1]
    # [0,0,-1]
    # 2、对差值平方
    # [0,0,1]
    # [1,1,1]
    # [0,0,1]
    # 3、将平方后的差值累加
    # [1]
    # [3]
    # [1]
    # 4、将上一步骤的值求开方，即得距离
    # [1]
    # [1.73]
    # [1]
    #
    # ]
    # tile(A, reps): 构造一个矩阵，通过A重复reps次得到
    # the following copy numSamples rows for dataSet
    diff = tile(newInput, (numSamples, 1)) - dataSet  # 按元素求差值
    squaredDiff = diff ** 2  # 将差值平方
    squaredDist = sum(squaredDiff, axis = 1)   # 按行累加
    distance = squaredDist ** 0.5  # 将差值平方和求开方，即得距离

    # # step 2: 对距离排序
    # argsort() 返回排序后的索引值
    sortedDistIndices = argsort(distance)
    classCount = {} # define a dictionary (can be append element)
    for i in range(k):
        # # step 3: 选择k个最近邻
        voteLabel = labels[sortedDistIndices[i]]

        # # step 4: 计算k个最近邻中各类别出现的次数
        # when the key voteLabel is not in dictionary classCount, get()
        # will return 0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    # # step 5: 返回出现次数最多的类别标签
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex
