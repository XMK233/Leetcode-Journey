# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/28eb3175488f4434a4a6207f6f484f47?tpId=117&&tqId=37752&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
编写一个函数来查找字符串数组中的最长公共前缀。
示例1
输入
复制
["abca","abc","abca","abc","abcc"]
返回值
复制
"abc"

参考的解法相当于是暴力解法，也就是拿第一个字符串来遍历。

'''

#
#
# @param strs string字符串一维数组
# @return string字符串
#
class Solution:
    def longestCommonPrefix(self , strs ):
        result = ''
        if strs == []:
            return result
        elif len(strs)<2:
            return strs[0]
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if len(j) == i or ( not strs[0][i] == j[i] ) :
                    return result
            result += strs[0][i]
            #print(strs,result)
        return result