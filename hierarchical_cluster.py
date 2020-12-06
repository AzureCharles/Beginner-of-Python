# Hierarchical cluster
from math import sqrt
def pearson(v1, v2):
    sum1 = sum(v1)
    sum2 = sum(v2)

    sum1Sq = sum([pow(v, 2) for v in v1])
    sum2Sq = sum([pow(v, 2) for v in v2])

    pSum = sum([v1[i] * v2[i] for i in range(len(v1))])

    num = pSum - ((sum1 * sum2) / len(v1))
    den = sqrt((sum1Sq - pow(sum1, 2) / len(v1)) * (sum2Sq - pow(sum2, 2) / len(v1)))

    if den == 0:
        return 0.0
    return 1.0 - num / den


def readfile(filename):
    lines = [line for line in open(filename)]
    # 第一行是列标题
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        # 每行的第一列是列名
        rownames.append(p[0])
        # 剩余部分就是该行对应的数据
        data.append([float(x) for x in p[1:]])
    return rownames, colnames, data

class bicluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.vec = vec
        self.right = right
        self.distance = distance
        self.id = id


def hcluster(rows, distance=pearson):
    distances = {}
    currentclustid = -1
    lowestpair = None

    # 最开始的聚类就是数据集中的行
    clusts = [bicluster(rows[i], id=i) for i in range(len(rows))]

    while len(clust) > 1:
        closest = distance(clusts[0].vec, clusts[1].vec)
        # 遍历每一个配对，寻找最小距离
        for i in range(len(clusts) - 1):
            for j in range(i+1, len(clusts)):
                # 用distances来缓存距离的计算值
                if distances.get((clusts[i].id, clusts[j].id)) is None:
                    distances[(clusts[i].id, clusts[j].id)] = distance(clusts[i].vec, clusts[j].vec)
                d = distances[(clusts[i].id, clusts[j].id)]
                # 寻找最相似的两个群组
                if d < closest:
                    closest = d
                    lowestpair = (i, j)
        bic1, bic2 = lowestpair
        # 计算两个聚类的平均值
        mergevec = [((clusts[bic1].vec[i] + clusts[bic2].vec[i]) / 2.0) for i
                    in range(len(clusts[bic1].vec))]
        # 建立新的聚类
        newcluster = bicluster(mergevec, left=clusts[bic1], right=clusts[bic2], distance=closest,
                               id=currentclustid)
        # 不在原始集合中的聚类，其id为负数
        currentclustid -= 1
        del clusts[bic2]
        del clusts[bic1]
        clusts.append(newcluster)
    return clusts[0]


#这次要用到PIL(Python Imaging Library)函数库，可以直接使用命令行pip install Pillow安装该库。
def getheight(clust):
    # 这是一个叶节点吗？若是，则高度为1
    if clust.left is None and clust.right is None:
        return 1
    # 否则，高度为每个分支的高度之和
    return getheight(clust.left)+getheight(clust.right)

def getdepth(clust):
    # 一个叶节点的距离是0.0
    if clust.left is None and clust.right is None:
        return 0
    # 一个枝节点的距离等于左右两侧分支中距离较大者，加上该枝节点自身的距离
    return max(getdepth(clust.left), getdepth(clust.right)) + clust.distance

