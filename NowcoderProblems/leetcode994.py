'''
https://leetcode-cn.com/problems/rotting-oranges/submissions/

994. 腐烂的橘子
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。



示例 1：



输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。


提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2

'''

class Solution:
    def orangesRotting(self, grid) -> int:
        ## 初始分钟是-1
        minutes = -1
        ## 是一个栈,用来做BFS的标配栈.
        stack = []
        ## BFS有点像按层遍历二叉树, 而lastcord是用来指示某一层的最后一个节点的. lastCord这个节点出去后, 一层的节点就全都遍历完了.
        lastCord = None
        directions = {
            "up" : (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)

        }
        ## 第一遍遍历grid, 将初始是腐烂的橘子都给他找出来.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append((i, j))
                    lastCord = (i, j)
        ## 然后就是用stack进行BFS遍历.
        while len(stack) > 0:
            cord = stack.pop(0)
            rotOrangeRow = cord[0]
            rotOrangeCol = cord[1]
            for i in directions:
                newPosRow = rotOrangeRow + directions[i][0]
                newPosCol = rotOrangeCol + directions[i][1]
                ## 如果腐烂的橘子周边有好的橘子, 就要变成坏橘子咯.
                if newPosRow >= 0 and newPosRow < len(grid) and newPosCol >= 0 and newPosCol < len(grid[0]) and grid[newPosRow][newPosCol] == 1:
                    stack.append((newPosRow, newPosCol))
                    grid[newPosRow][newPosCol] = 2
            ## 如果一层遍历完, 那么就要进入下一层, 也就是分钟数要增加1了.
            if cord == lastCord:
                minutes += 1
                if len(stack) >= 1:
                    lastCord = stack[-1]
                else:
                    pass
        ## 再遍历一遍grid, 如果有一些地方还有没腐烂的橘子, 直接返回-1; 如果所有的橘子都腐烂了, 就返回分钟数;
        ## 小心有一种情况, 就是原grid上没有任何橘子, 那么这种情况理论上是要返回0的,而非 -1.
        sumOfGrid = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sumOfGrid += grid[i][j]
                if grid[i][j] == 1:
                    return -1
        if sumOfGrid == 0:
            return 0
        else:
            return minutes

print(Solution().orangesRotting(
    [[0,2]]
))