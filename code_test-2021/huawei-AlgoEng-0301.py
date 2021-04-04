'''
班上有N个学生, 有一些人是朋友, 有些不是. 他们的友谊是具有传递性的.
如果A是B的朋友, B是C的朋友, 那么A与C也就是朋友了. 所谓朋友圈, 就是朋友的集合.

给定一个N维方阵M, 表示班级中学生之间的朋友关系. M[i][j] = 1说明i与j的朋友互为朋友关系. 否则就是朋友关系未知.

请输出朋友圈的总数.

[
[1, 1, 0]
[1, 1, 0]
[0, 0, 1]
]
这里面有两个, AB和C是两个朋友圈.

下面的例子, 就是程序里面跑的那个M啊, 就只有1个朋友圈了.

我的思路是怎么解的呢?
从第一个没访问过的1开始访问, 然后使用DFS, 具体怎么DFS呢? 如果它的右边或者下边只要有朋友(同一行右边以及同一列下边)且没访问过, 就往那里走,
然后标记那里访问过了.
DFS结束之后, 这个访问的起点所在的朋友圈就都被访问过了, 并且都标记上了访问过了的标志.
然后再找一个没访问过的1开始再来DFS, 这样就是新的一个朋友圈开始了.
'''


M = [
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

visited = [[False] * len(M[0]) for _ in range(len(M))]

numFriendCircle = 0

def findNumFriendCircle(i, j):
    visited[i][j] = True
    visited[j][i] = True
    for x in range(1, len(M[0]) - j):
        if M[i][j + x] == 1 and not visited[i][j + x]:
            findNumFriendCircle(i, j + x)
    for y in range(1, j - i + 1):
        if M[i + y][j] == 1 and not visited[i + y][j]:
            findNumFriendCircle(i + y, j)


for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == 1 and not visited[i][j]:
            ## 0, 0
            numFriendCircle += 1
            findNumFriendCircle(i, j)

print(numFriendCircle)