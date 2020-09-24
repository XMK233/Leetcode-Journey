#### 提交的输入输出方式
# n = int(input())
# plate = []
# for i in range(n):
#     line = input()
#     plate.append([int(_) for _ in line.strip().split()])
#####在本地测试用的数据
n = 3
plate = [
    [1, 2, 4],
    [1, 3, 1],
    [1, 2, 1]
]
########dfs方法, 递归层数超限.
# record = [[float("Inf")] * n for _ in range(n)]
# directions = [
#     (-1, 0), (1, 0), (0, -1), (0, 1)
# ]
# def dfs(plate, startR, startC, tgtR, tgtC):
#     minDistance = float("Inf")
#     for d in directions:
#         newR, newC = startR + d[0], startC + d[1]
#         if newR >= 0 and newR <= n - 1 and newC >= 0 and newC <= n - 1:
#             ## 能走.
#             distance = float("Inf")
#             if record[newR][newC] == float("Inf"):
#                 distance = dfs(plate, newR, newC, tgtR, tgtC) + abs(plate[newR][newC] - plate[startR][startC])
#             else:
#                 distance = record[newR][newC] + abs(plate[newR][newC] - plate[startR][startC])
#             # if distance < minDistance:
#             minDistance = min(minDistance, distance)
#     record[startR][startC] = minDistance
#     return minDistance
# dfs(plate, 0, 0, n-1, n-1)
# print(record)
########dp方法, 可行, 但是没写完. 这种写法得到的结果不是
dp = [[-1] * n for _ in range(n)]
dp[0][0] = 0

def helper(plate, dp):
    ## 第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + abs(plate[0][j] - plate[0][j - 1])
    ## 后面的行
    for i in range(1, n):
        for j in range(n):
            ## 第一列
            if j == 0:
                dp[i][j] = dp[i - 1][j] + abs(plate[i][j] - plate[i - 1][j])
            ## 后面的列
            else:
                dp[i][j] = min(dp[i - 1][j] + abs(plate[i][j] - plate[i - 1][j]), dp[i][j - 1] + abs(plate[i][j] - plate[i][j - 1]))

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

#######################
helper(plate, dp)
print(dp)