## 最长公共子序列
n = int(input())
firstPerson = input().split()
secondPerson = input().split()
# n = 7
# firstPerson = "a b c d e f g".split()
# secondPerson = "b d a c f g e".split()
dp = [[0]* n for i in range(n)]

## 处理第一行
for j in range(n):
    if j == 0:
        dp[0][0] = 0 if firstPerson[0] != secondPerson[0] else 1
    else:
        if firstPerson[j] == secondPerson[0]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j - 1]
## 处理第一列
for i in range(1, n):
    if firstPerson[0] == secondPerson[i]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i - 1][0]

for i in range(1, n):
    for j in range(1, n):
        ###
        if firstPerson[j] == secondPerson[i]:
            dp[i][j] = max (1 + dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        ##
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# for line in dp:
#     print(line)
print(dp[n-1][n-1])