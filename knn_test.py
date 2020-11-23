#!/usr/bin/python
# coding=utf-8
import knn_example
import numpy as np
import random as rd
from numpy import *
# 生成数据集和类别标签
dataSet, labels = knn_example.createDataSet()
k = 7
"""
# 以下为特例测试
# 定义一个未知类别的数据
test_target = array([23, 3, 17])
k = 3
# 调用分类函数对未知数据分类
outputLabel = knn_example.kNNClassify(test_target, dataSet, labels, 3)
print("Your input is:", test_target, "and classified to class: ", outputLabel)

test_target = array([25, 27, 12])
outputLabel = knn_example.kNNClassify(test_target, dataSet, labels, 3)
print("Your input is:", test_target, "and classified to class: ", outputLabel)
"""

def quickExampleSet(label_set):
    #label_set是指定的类别标签列表
    q_example = [rd.randint(0,100) for i in range(3)]
    max_index = q_example.index(max(q_example))
    for lb in label_set:
        if max_index == label_set.index(lb):
            
            q_example.append(lb)
    return q_example
    
def knnTestFunction(test_times,setted_labels,k):
    end_flag = 0
    count = 0
    while end_flag <= test_times:
        quick_example = quickExampleSet(setted_labels)
        test_target = array(quick_example[:3])
        outputLabel = knn_example.kNNClassify(test_target, dataSet, labels, k)
        if outputLabel == quick_example[-1]:
            count += 1
        #print(quick_example)
        end_flag += 1
    return count/test_times
    
#test_times = int(input("How many times do you want for the iteration:"))
test_times = 1000

setted_labels = list(set(labels))
results = []
for t in range(10):
    results.append(knnTestFunction(test_times,setted_labels,k))
    print("While k=", k, ",the accuracy rate is:", knnTestFunction(test_times,setted_labels,k)*100,
          "% (",test_times, "times )" )
print("The variance is ", np.var(results))     
