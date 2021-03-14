# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c4c488d4d40d4c4e9824c3650f7d5571?tpId=117&&tqId=37843&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
以字符串的形式读入两个数字，编写一个函数计算它们的乘积，以字符串形式返回。
（字符串长度不大于10000，保证字符串仅由'0'~'9'这10种字符组成）
示例1
输入
复制
"11","99"
返回值
复制
"1089"
说明
11*99=1089

python是没有大数之忧的，很叼吧？
'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param s string字符串 第一个整数
# @param t string字符串 第二个整数
# @return string字符串
#
class Solution:
    def solve(self , s , t ):
        # write code here
        return str(int(s) * int(t))
