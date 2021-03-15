# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/0c9664d1554e466aa107d899418e814e?tpId=117&&tqId=37833&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数。
示例1
输入
复制
[[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]]
返回值
复制
3
备注:
01矩阵范围<=200*200

应该就是典型的dfs了.
'''
class Solution:
    def solve(self , grid ):
        r , c = len(grid) , len(grid[0])
        if r==0 or c ==0: return 0

        def dfs(grid, i, j):
            grid[i][j] = 0 ## 直接修改原来的grid, 把1的地方改为0, 就算是走过了.
            r, c = len(grid), len(grid[0])
            for i, j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= i < r and 0 <= j < c and grid[i][j] == '1':
                    dfs(grid, i, j)

        nums = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    nums += 1
                    dfs(grid , i , j)
        return nums
