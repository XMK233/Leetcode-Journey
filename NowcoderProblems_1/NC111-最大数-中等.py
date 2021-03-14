# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/fc897457408f4bbe9d3f87588f497729?tpId=117&&tqId=37835&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个数组由一些非负整数组成，现需要将他们进行排列并拼接，使得最后的结果最大，返回值需要是string类型 否则可能会溢出
示例1
输入
复制
[30,1]
返回值
复制
"301"
备注:
输出结果可能非常大，所以你需要返回一个字符串而不是整数。

剑指offer45题
'''

import functools
class Solution:
    def minNumber(self, nums):
        # write code here
        if not nums:
            return ""
        arr = list(str(x) for x in nums)
        def f(a,b):
            if a+b<b+a:
                return -1
            else:
                return 1
        arr.sort(key=functools.cmp_to_key(f), reverse=True)
        return str(int("".join(arr))) ## 这里为什么这么骚？为防止输入【0，0】导致输出为“00”的情况。
