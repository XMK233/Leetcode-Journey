class Solution:
    def generateParenthesis(self , n: int):
        # write code here
        res = []
        if not n:
            return res
        def helper(l, r, s):
            if r < l:
                return
            if l == 0 and r == 0:
                res.append(s)
            if l > 0:
                helper(l-1, r, s + "(")
            if r > 0:
                helper(l, r-1, s + ")")

        helper(n, n, "")
        return res

print(
    Solution().generateParenthesis(3)
)
'''
描述
给出n对括号，请编写一个函数来生成所有的由n对括号组成的合法组合。
例如，给出n=3，解集为：
"((()))", "(()())", "(())()", "()()()", "()(())"

数据范围：0 \le n \le 100≤n≤10
要求：空间复杂度 O(n!)O(n!)，时间复杂度 O(n!)O(n!)
示例1
输入：
1
复制
返回值：
["()"]
复制
示例2
输入：
2
复制
返回值：
["(())","()()"]
'''