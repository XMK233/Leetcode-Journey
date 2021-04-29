# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=117&&tqId=37764&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0 or number == 1:
            return 1
        ## 
        i = 2
        a = 1
        b = 1
        while i <= number:
            tmp = b
            b = a + b
            a = tmp
            i += 1
        return b
