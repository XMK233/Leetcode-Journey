# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/9ce534c8132b4e189fd3130519420cde?tpId=117&&tqId=37825&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
从0,1,2,...,n这n+1个数中选择n个数，组成有序数组，请找出缺失的那个数，要求O(n)尽可能小。
示例1
输入
复制
[0,1,2,3,4,5,7]
返回值
复制
6

'''
#
# 找缺失数字
# @param a int整型一维数组 给定的数字串
# @return int整型
#
class Solution:
    def solve(self , a ):
        # write code here
        nums = a
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i