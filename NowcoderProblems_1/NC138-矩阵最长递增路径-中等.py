# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/7a71a88cdf294ce6bdf54c899be967a2?tpId=117&&tqId=37850&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个矩阵，矩阵内所有数均为非负整数。
求一条路径，该路径上所有数是递增的。
这个路径必须满足以下条件：
1、对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外。
2、你不能走重复的单元格。即每个格子最多只能走一次。
示例1
输入
复制
[[1,2,3],[4,5,6],[7,8,9]]
返回值
复制
5
说明
1->2->3->6->9即可。当然这种递增路径不是唯一的。
示例2
输入
复制
[[1,2],[4,3]]
返回值
复制
4
说明
 1->2->3->4

备注:
矩阵的长和宽均不大于1000，矩阵内每个数不大于1000

用DFS算法。还算直白，直接看代码就懂了，掌声。

'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#

from pprint import pprint
class Solution:
    def solve(self , matrix ):
        # write code here
        cols = len(matrix[0])
        rows = len(matrix)
        dp = [[0] * cols for _ in range(rows)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  ## up, down left, right
        maxLen = 0

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] = 1 ## 这一行说明了，其实dp里面，初始化的时候是0，不过一旦这个点走过，那么这个点的dp值必然是大于0的，至少为1.
            for direction in dirs:
                nx = i + direction[0]
                ny = j + direction[1] ## 这里i写程j了。这就是我写代码的一个问题，就是手速上去了，脑子还没跟上，没法确定自己写的都是对的。
                if (nx >= 0 and nx <= rows - 1) and (ny >= 0 and ny <= cols - 1) and (matrix[nx][ny] > matrix[i][j]):
                    dp[i][j] = max(dp[i][j], 1 + dfs(nx, ny))
            return dp[i][j]

        for i in range(rows):
            for j in range(cols):
                maxLen = max(maxLen, dfs(i, j))
        return maxLen


print(Solution().solve([[1,2], [4, 3]]))