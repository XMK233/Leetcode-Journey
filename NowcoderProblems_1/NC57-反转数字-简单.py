# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/1a3de8b83d12437aa05694b90e02f47a?tpId=117&&tqId=37755&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
将给出的32位整数x翻转。
例1:x=123，返回321
例2:x=-123，返回-321

你有注意到翻转后的整数可能溢出吗？因为给出的是32位整数，则其数值范围为[−2^{31}, 2^{31} − 1][−2
31
 ,2
31
 −1]。翻转可能会导致溢出，如果反转后的结果会溢出就返回 0。

示例1
输入
复制
-123
返回值
复制
-321

python不用考虑溢出的问题.
主要是你要懂得怎么倒序一个字符串: [::-1]
'''
class Solution:
    def reverse(self , x ):
        # write code here
        return -(int(str(abs(x))[::-1])) if x<0 else int(str(x)[::-1])