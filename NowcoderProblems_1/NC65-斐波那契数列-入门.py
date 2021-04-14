# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=117&&tqId=37760&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n\leq 39n≤39

示例1
输入
复制
4
返回值
复制
3

没什么可说的了.
'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0, 1]
        i = 2
        while i <= n:
            res.append(res[i - 1] + res[i - 2])
            i = i + 1
        return res[n]