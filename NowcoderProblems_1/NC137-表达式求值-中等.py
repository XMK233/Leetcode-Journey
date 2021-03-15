# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c215ba61c8b1443b996351df929dc4d4?tpId=117&&tqId=37849&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
请写一个整数计算器，支持加减乘三种运算和括号。
示例1
输入
复制
"1+2"
返回值
复制
3
示例2
输入
复制
"(2*(3-4))*5"
返回值
复制
-10
示例3
输入
复制
"3+2*3*4-1"
返回值
复制
26

如果是python可以直接用eval()来跑. 如果不用这种方法, 可以使用栈来做.
'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class Solution:
    def solve(self , s ):
        # write code here
        return(eval(s))