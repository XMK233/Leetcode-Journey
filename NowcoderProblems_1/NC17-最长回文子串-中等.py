# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/b4525d1d84934cf280439aeecc36f4af?tpId=117&&tqId=37789&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。

给定字符串A以及它的长度n，请返回最长回文子串的长度。

示例1
输入
复制
"abc1234321ab",12
返回值
复制
7
'''
class Solution:
    def getLongestPalindrome(self, A, n):
        def func(A, left, right):
            while left >= 0 and right < n and A[left] == A[right]:
                left -= 1
                right += 1
            return right - left - 1

        res = 0
        for i in range(n - 1):
            res = max(res, func(A, i, i), func(A, i, i + 1))
        return res