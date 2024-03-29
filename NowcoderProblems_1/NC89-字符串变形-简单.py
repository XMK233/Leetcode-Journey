# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c3120c1c1bc44ad986259c0cf0f0b80e?tpId=117&&tqId=37792&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
对于一个给定的字符串，我们需要在线性(也就是O(n))的时间里对它做一些变形。首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把着个字符串中由空格隔开的单词反序，同时反转每个字符的大小写。比如"Hello World"变形后就变成了"wORLD hELLO"。

输入描述:
给定一个字符串s以及它的长度n(1≤n≤500)
返回值描述:
请返回变形后的字符串。题目保证给定的字符串均由大小写字母和空格构成。
示例1
输入
复制
"This is a sample",16
返回值
复制
"SAMPLE A IS tHIS"

主要是使用swapcase()方法。

'''

class Solution:
    def trans(self, s, n):
        # write code here
        upperVersion = [i.swapcase() for i in s.split(" ")]
        return " ".join(upperVersion[::-1])

print(Solution().trans(" h I",4))