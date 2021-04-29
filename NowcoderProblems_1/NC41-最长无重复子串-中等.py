# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/b56799ebfd684fb394bd315e89324fb4?tpId=117&&tqId=37816&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
示例1
输入
复制
[2,3,4,5]
返回值
复制
4
示例2
输入
复制
[2,2,3,4,3]
返回值
复制
3
'''


#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr):
        # write code here
        s = arr
        """
        :type s: str
        :rtype: int
        """
        head = 0
        longest = 0
        dic = {}  # 存放的是字符，以及字符在字符串中的序号。

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= head:  # 如果这个字符是重复的字符，并且上一次出现在head之后，
                head = dic[s[i]] + 1  # 才需要移动head
            dic[s[i]] = i  # 否则一律按新出现字符来看待。
            longest = max((i - head + 1), longest)  # 看看最大长度有没有更新

        return longest