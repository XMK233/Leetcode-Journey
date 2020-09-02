## n是行数, m是列数.
## 问, 把任意一个1移动到任意的0上, 求这样一来构成的联通的1的区域最大是多少.
## 技巧: 从一个0出发, 做dfs, 然后统计联通的1有多少.
## 如果从0出发联通的1的个数小于总数, 就用这个数; 如果大于总数(因为我的算法是把出发点也算是1), 那么就返回总数.
## 没有AC, 估计是超时或者超内存了. 过了四成五.
n, m = 4, 4
plate = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
]
################
directions = [
    (0, -1), (0, 1), (-1, 0), (1, 0)
]

def dfs(plate, i, j, visited):
    # visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1 ## 自己已经访问过了
    soldiers = 1 ## 自己要先算进去.
    for d in directions:
        newI, newJ = i + d[0], j + d[1]
        if newI >= 0 and newI <= n - 1 and newJ >= 0 and newJ <= m - 1: ### 在棋盘中.
            if plate[newI][newJ] == 1 and visited[newI][newJ] == 0:
                soldiers += dfs(plate, newI, newJ, visited)
    return soldiers

allNum = 0
for i in range(n):
    for j in range(m):
        allNum += plate[i][j]

maxNum = -1
for i in range(n):
    for j in range(m):
        if plate[i][j] == 0: ## 看每一个0点.
            visited = [[0] * m for _ in range(n)]
            possible = dfs(plate, i, j, visited)
            if possible > maxNum:
                maxNum = possible

print(min(maxNum, allNum))