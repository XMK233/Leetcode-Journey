# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/fd711bdfa0e840b381d7e1b82183b3ee?tpId=117&&tqId=37809&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定String类型的数组strArr，再给定整数k，请严格按照排名顺序打印 出次数前k名的字符串。
[要求]
如果strArr长度为N，时间复杂度请达到O(N \log K)O(NlogK)

输出K行，每行有一个字符串和一个整数（字符串表示）。
你需要按照出现出现次数由大到小输出，若出现次数相同时字符串字典序较小的优先输出

示例1
输入
复制
["1","2","3","4"],2
返回值
复制
[["1","1"],["2","1"]]
示例2
输入
复制
["1","1","2","3"],2
返回值
复制
[["1","2"],["2","1"]]
备注:
1 \leq N \leq 10^51≤N≤10
5

很简单的hash方法. 统计个数然后排序就好了.

'''
#
# return topK string
# @param strings string字符串一维数组 strings
# @param k int整型 the k
# @return string字符串二维数组
#
import collections
class Solution:
    def topKstrings(self , strings , k ):
        # write code here
        strings = sorted(strings)
        freq = collections.defaultdict(int)
        for s in strings:
            freq[s] += 1
        ret = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ret_final = []
        for i in ret:
            if k > 0:
                ret_final.append([str(i[0]), str(i[1])])
            else:
                break
            k -= 1
        return ret_final