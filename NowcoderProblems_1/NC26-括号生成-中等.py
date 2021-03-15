# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c9addb265cdf4cdd92c092c655d164ca?tpId=117&&tqId=37748&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出n对括号，请编写一个函数来生成所有的由n对括号组成的合法组合。
例如，给出n=3，解集为：
"((()))", "(()())", "(())()", "()()()", "()(())",
示例1
输入
复制
1
返回值
复制
["()"]
示例2
输入
复制
2
返回值
复制
["(())","()()"]

'''


#
#
# @param n int整型
# @return string字符串一维数组
#
class Solution:
    def generateParenthesis(self, n):
        self.res = []

        def gen(p, left, right): ## left, right就是指左右括号的剩余数量.
            if left == 0 and right == 0:
                self.res.append(p)
            if left < 0 or right < 0: ## 左括号数或者右括号数用完了, GG.
                return
            if left > right: ## 右括号数更少了, 那也得GG.
                return
            gen(p + "(", left - 1, right) ## 这里用: p+"(" 进入循环, 而不是先p += "("再用p进入循环. 参考代码的这个操作, 本身就是有回溯的意味.
            gen(p + ")", left, right - 1)

        gen("", n, n)
        return self.res

print(Solution().generateParenthesis(1))