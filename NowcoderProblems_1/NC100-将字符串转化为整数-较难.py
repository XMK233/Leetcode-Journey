# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/44d8c152c38f43a1b10e168018dcc13f?tpId=117&&tqId=37754&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
实现函数 atoi 。函数的功能为将字符串转化为整数
提示：仔细思考所有可能的输入情况。这个问题没有给出输入的限制，你需要自己考虑所有可能的情况。



示例1
输入
复制
"123"
返回值
复制
123

剑指offer67.
暴力解就好了.
'''
#
#
# @param str string字符串
# @return int整型
#
class Solution:
    def atoi(self , str ):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.strip()
        if len(str) == 0:
            return 0
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >= '0' and c <= '9':
                number = 10*number + int(c) ##ord(c) - ord('0')
            else:
                break
        number = flag * number
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number