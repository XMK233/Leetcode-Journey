# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/45fd68024a4c4e97a8d6c45fc61dc6ad?tpId=117&&tqId=37745&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出一个仅包含字符'('和')'的字符串，计算最长的格式正确的括号子串的长度。
对于字符串"(()"来说，最长的格式正确的子串是"()"，长度为2.
再举一个例子：对于字符串")()())",来说，最长的格式正确的子串是"()()"，长度为4.
示例1
输入
复制
"(()"
返回值
复制
2

dp[i]表示以i结尾最长合法字符串。
如果s[i]=='('时该字符串一定不合法；当s[i]==')'时，假设存在解，那么该右括号与其对应的左括号之间的字符串一定是合法的。
因此对于i-1的位置，以i-1结尾的合法字符串的开头下标为i - dp[i - 1]，当其前一个位置s[i - 1 - dp[i - 1]] == '('时，可以与s[i]进行匹配，dp[i]更新为dp[i - 1] + 2。
此时还需要注意，如果在与当前右括号匹配的左括号的前一个位置(i - 1 - dp[i - 1]) - 1，以该处为结尾的最长合法字符串不为0，也需要加到结果上。例如()()。

参考的做法，实现了上述题解。
'''
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def longestValidParentheses(self , s ):
        # write code here
        if not s:
            return 0
        n=len(s)
        dp=[0]*n
        for i in range(1,n):
            if s[i]=='(':
                continue
            j=i-dp[i-1]-1
            if s[j]=='(':
                if j>0:
                    dp[i]=2+dp[i-1]+dp[j-1]
                else:
                    dp[i]=2+dp[i-1]
        return max(dp)
