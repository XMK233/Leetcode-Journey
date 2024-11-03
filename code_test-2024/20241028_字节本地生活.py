## 出了一个题目，就是最大岛屿问题。
## 当天晚上面试的，没有做出来，第二天做出来了。。。
## 或许是晚上状态不好，抑或是练习太少，反正临场是做不出来的。
## 第二天，我上网搜出来这个题 https://zhuanlan.zhihu.com/p/609176782
## 然后纯自己实现了一波，做出来了。反正例题能做对，至于oj能不能全部pass，就没再去试验了。
## 当天想的时候，没想明白怎么设计递归。第二天想明白了。
## 首先，每一个1只能属于一个岛屿，如果一个1属于俩岛屿，那实际上你以为的俩岛屿本质就是一个岛屿。
## 然后就是，探索过的岛屿标记为0就好了，不必再去探索。
## 所以递归设计就是，从某一个1的点出发，上下左右去做递归，递归的过程中，如果遇到1就记录面积，然后标记为0，如果遇到0就直接返回面积为0.
## 然后退出递归，把上下左右四个方向的面积加起来，就是这个1所在岛屿的最大面积。
## 然后对grid中的每一个1去做上述递归，就能找到最大的面积。

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

##

class Solution1:
    symb = []
    res = 0
    def __init__(self, grid):
        self.symb = [
            [0 for _ in range(len(grid[0]))] for __ in range(len(grid))
        ]
    def helper(self, grid, i, j):
        '''判断一下，从i，j出发能够返回出多大的面积。'''
        if grid[i][j] == 0:
            return 0
        if (grid[i][j] == 1) and (self.symb[i][j] == 1):
            return 0
        ####################
        res_here = 0
        if (grid[i][j] == 1) and (self.symb[i][j] == 0):
            res_here += 1
            self.symb[i][j] = 1
        if i + 1 < len(grid):
            res_here += self.helper(grid, i+1, j)
        if i - 1 >= 0:
            res_here += self.helper(grid, i-1, j)
        if j + 1 < len(grid[0]):
            res_here += self.helper(grid, i, j+1)
        if j - 1 >= 0:
            res_here += self.helper(grid, i, j-1)
        return res_here

    def get_the_biggest_island_area(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.res = max(self.helper(grid, i, j), self.res)
        return self.res

s = Solution1(grid)
print(s.get_the_biggest_island_area(grid))

class Solution2:
    res = 0
    def helper(self, grid, i, j):
        '''判断一下，从i，j出发能够返回出多大的面积。'''
        if grid[i][j] == 0:
            return 0
        ####################
        res_here = 0
        if (grid[i][j] == 1):
            res_here += 1
            grid[i][j] = 0
        if i + 1 < len(grid):
            res_here += self.helper(grid, i+1, j)
        if i - 1 >= 0:
            res_here += self.helper(grid, i-1, j)
        if j + 1 < len(grid[0]):
            res_here += self.helper(grid, i, j+1)
        if j - 1 >= 0:
            res_here += self.helper(grid, i, j-1)
        return res_here

    def get_the_biggest_island_area(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.res = max(self.helper(grid, i, j), self.res)
        return self.res

s = Solution2()
print(s.get_the_biggest_island_area(grid))