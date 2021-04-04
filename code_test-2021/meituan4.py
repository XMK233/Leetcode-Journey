'''

小美的跳方格
时间限制： 3000MS
内存限制： 589824KB
题目描述：
小美在路上看到一些小学生在玩跳方格，她也想跟着一起玩。

这个方格被划分为n×n的小方格，即有n行n列。每一个小方格上面都是一个1~k的正整数。小美想依次从1,2,…,k这个顺序来跳。一开始小美可以站在任意一个小方格。从一个方格跳到另一个方格的花费为两个方格的曼哈顿距离。小美想知道是否可以依照该顺序一直跳到k，如果可以，最小的总花费是多少。

两个格子(x1,y1),(x2,y2)的曼哈顿距离为：|x1-x2|+|y1-y2|。例如(3,4),(1,6)的曼哈顿距离为|3-1|+|4-6|=4。



输入描述
第一行两个正整数n,k；

接下来n行n列，表示该方格。每个数字都在1~k的范围内。

1≤n≤50，1≤k≤n2

输出描述
如果不可能完成，输出-1；否则，输出最小总花费。


样例输入
2 2
1 2
2 1
样例输出
1

提示
小美从(1,1)跳到(1,2)，花费为1。

输入样例2
	4 4
	1 2 2 1
	2 4 4 1
	4 4 4 2
	1 1 1 2
输出样例2
	-1
样例解释2
	小美不可能依照该顺序跳到4。

'''
# n, k = [int(_) for _ in input().strip().split()]
# board = []
# for i in range(n):
#     board.append([int(_) for _ in input().strip().split()])
#####
# n, k = 4, 4
# board = [
#     [1, 2, 2, 1],
#     [2, 3, 4, 1],
#     [4, 4, 4, 2],
#     [1, 1, 1, 2]
# ]
n, k = 2, 2
board = [
    [1, 2],
    [2, 1]
]
#######################
directions = [
    (-1, 0), ## up
    (1, 0), ## down
    (0, -1), ## left
    (0, 1) ## right
]
partRes = [[float("Inf")] * n for i in range(n)]
def dfs(i, j, m):
    if partRes[i][j] != float("Inf"):
        return partRes[i][j]
    if board[i][j] == k:
        return 0
    res = float("Inf")
    newNum = m + 1
    for direction in directions:
        newRow = i + direction[0]
        newCol = j + direction[1]
        if 0<=newRow<=n-1 and 0<=newCol<=n-1 and board[newRow][newCol] == newNum:
            res = min(res, 1 + dfs(newRow, newCol, newNum))
    partRes[i][j] = res
    return res

minRes = float("Inf")
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            minRes = min(minRes, dfs(i, j, 1))
if minRes == float("Inf"):
    print(-1)
else:
    print(minRes)