# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/2baf799ea0594abd974d37139de27896?tpId=117&&tqId=37851&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个数组，请你编写一个函数，返回该数组排序后的形式。
示例1
输入
复制
[5,2,3,1,4]
返回值
复制
[1,2,3,4,5]
示例2
输入
复制
[5,1,6,2,5]
返回值
复制
[1,2,5,5,6]

'''
class Solution:
    def MySort(self , arr ):
        # write code here
        return sorted(arr)