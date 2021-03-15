# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/2cc32b88fff94d7e8fd458b8c7b25ec1?tpId=117&&tqId=37836&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

进制转换.

用的是小学学过的方法. 不过我参考的这位, 将数字转为字符串的方法倒是很方便, 值得学习.
'''
#
# 进制转换
# @param M int整型 给定整数
# @param N int整型 转换到的进制
# @return string字符串
#
class Solution:
    def solve(self , M , N ):
        # write code here
        t="0123456789ABCDEF"
        flag=False
        if M==0:return "0"
        res=''
        if M<0:
            flag=True
            M=-M
        while M>0:
            res+=t[M%N]
            M//=N
        if flag:
            res+='-'
        return res[::-1]