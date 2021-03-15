# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/05fed41805ae4394ab6607d0d745c8e4?tpId=117&&tqId=37801&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定两个字符串str1和str2，再给定三个整数ic，dc和rc，分别代表插入、删除和替换一个字符的代价，请输出将str1编辑成str2的最小代价。
示例1
输入
复制
"abc","adc",5,3,2
返回值
复制
2
示例2
输入
复制
"abc","adc",5,3,100
返回值
复制
8

递推公式:
cost = 0 if str1[i] == str2[j] else rc
dp[i][j] = min(dp[i][j - 1] + ic, dp[i - 1][j] + dc, dp[i - 1][j - 1] + cost)
参考的实现, 不够优雅. 但是功能估计是完整的.
'''
#
# min edit cost
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @param ic int整型 insert cost
# @param dc int整型 delete cost
# @param rc int整型 replace cost
# @return int整型
#
class Solution:
    def minEditCost(self , str1 , str2 , ic , dc , rc ):
        # write code here
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(len(str1)):
            dp[i + 1][0] = dc * (i + 1)
        for i in range(len(str2)):
            dp[0][i + 1] = ic * (i + 1)
        for i in range(len(str1)):
            for j in range(len(str2)):
                cost = 0 if str1[i] == str2[j] else rc
                dp[i+1][j+1] = min(dp[i+1][j] + ic, dp[i][j+1] + dc, dp[i][j] + cost)
        return dp[-1][-1]