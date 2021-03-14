# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/8c5e99acb1fa4bc3a342cd321100c0cd?tpId=117&&tqId=37807&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
'''
题目描述
有一个源源不断的吐出整数的数据流，假设你有足够的空间来保存吐出的数。请设计一个名叫MedianHolder的结构，MedianHolder可以随时取得之前吐出所有数的中位数。
[要求]
1. 如果MedianHolder已经保存了吐出的N个数，那么将一个新数加入到MedianHolder的过程，其时间复杂度是O(logN)。
2. 取得已经吐出的N个数整体的中位数的过程，时间复杂度为O(1)

每行有一个整数opt表示操作类型
若opt=1，则接下来有一个整数N表示将N加入到结构中。
若opt=2，则表示询问当前所有数的中位数

示例1
输入
复制
[[1,5],[2],[1,3],[2],[1,6],[2],[1,7],[2]]
返回值
复制
[5,4,5,5.5]
说明
第一次查询时结构内的数为：5
第二次查询时结构内的数为：3 5
第二次查询时结构内的数为：3 5 6
第二次查询时结构内的数为：3 5 6 7

示例2
输入
复制
[[2],[1,1],[2]]
返回值
复制
[-1,1]

关键是用两个堆来存大的那一半和小的那一半.
记住heapq的关键性质: 堆化之后的数组, 左边总是存着最小的值, 也就是小顶堆, 顶部在数组左边.
大的那一半称为凤组, 小的那一半是鸡组. 凤组的元素个数总是大于等于鸡组.
怎么记住新元素应该加入到哪个数组呢? 诀窍: 这俩都想扩大领先优势.
1. 如果凤组多, 那么凤组要扩大领先优势, 所以先加入凤组.
2. 如果凤组和鸡组一样多, 那么鸡组要扩大或者说创造领先优势, 就要把新元素加入到鸡组.

'''


import heapq
class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 初始化大顶堆和小顶堆
        self.smallerHalf = []
        self.biggerHalf = []

    def addNum(self, num: int) -> None:
        if len(self.smallerHalf) == len(self.biggerHalf):  # 先加入鸡组，再把鸡组顶部元素加到凤组
            heapq.heappush(self.biggerHalf, -heapq.heappushpop(self.smallerHalf, -num))
        else:  # 先加到凤组，再把凤组顶部元素加入到鸡组
            heapq.heappush(self.smallerHalf, -heapq.heappushpop(self.biggerHalf, num))

    def findMedian(self) -> float:
        if len(self.biggerHalf) == len(self.smallerHalf):
            return (-self.smallerHalf[0] + self.biggerHalf[0]) / 2
        else:
            return self.biggerHalf[0]

    def flowmedian(self , operations ):
        res = []
        for operation in operations:
            if operation[0] == 1:
                self.addNum(operation[1])
            else:
                res.append(self.findMedian())
        return [float(a) for a in res]


print(Solution().flowmedian([[1,5],[2],[1,3],[2],[1,6],[2],[1,7],[2]]))