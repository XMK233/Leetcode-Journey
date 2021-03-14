# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/28970c15befb4ff3a264189087b99ad4?tpId=117&&tqId=37780&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
'''
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
示例1
输入
复制
"aaa","a*a"
返回值
复制
true

肯定是用dp来做了.

'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param pattern string字符串
# @return bool布尔型
#
class Solution:
    def match(self , str , pattern ):
        # write code here
        s = str
        p = pattern
        s, p = '#' + s, '#' + p
        m, n = len(s), len(p)
        dp = [[False] * n for _ in range(m)] ## dp的构建是, pattern横着摆, string纵向摆.
        dp[0][0] = True

        for i in range(m):
            for j in range(1, n):
                if i == 0:  ## dp数组第一行特殊对待
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j - 2]
                elif p[j] in [s[i], '.']: ## 如果碰上一样的字符或者是通配符
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*': ## 如果碰上*号, 有两种不同的对待方式, 分辨是 [(p[j - 1]与s[i]不同) or (相同)]
                    dp[i][j] = (j > 1 and dp[i][j - 2]) or (p[j - 1] in [s[i], '.'] and dp[i - 1][j])
                else: ## 如果碰上两个字符不一样, 直接GG咯. 
                    dp[i][j] = False
        return dp[-1][-1]