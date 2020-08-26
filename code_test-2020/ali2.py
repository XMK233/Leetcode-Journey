n = 5
a = [2, 5, 3, 1, 2]

## 原题: n是数组长度, a是数组.
### 然后, k取值为1到n.
### 相邻的k个数里面最小的那个数是为这k个数的一个能力值.
### 当k值取某一个值的时候, 把最大的能力值记录一下.
### 试求所有k个值各自的最大能力值.

### 啊啊啊啊啊, 做的时候, 时间不够, 于是慌不择路地选择了暴力解法.
### 然而暴力解法并不会更容易. 反倒有点难.
### 用最普通的动态规划可以解. 至少例题能过. 但是后续的也就没机会测试了.

dp = [[-1 for i in range(n)] for j in range(n)]
# dplist = [-1 for k in range(n)]
res = []
for k in range(0, n):
    for i in range(k, n):
        if k == 0: ## 第一行
            dp[k][i] = a[i]
        else: ## 后面的行
            dp[k][i] = min(dp[k - 1][i - 1], dp[k - 1][i])
    res.append(max(dp[k]))
print(res)