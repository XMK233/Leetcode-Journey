## 没做出来.

n, p = [int(_) for _ in input().split()]
dp = [[0] * (p + 1) for _ in range(n + 1)]
nums = []
prices = []
charms = []
for _ in range(n):
    num, price, charm = [int(_) for _ in input().split()]
    nums.append(num)
    prices.append(price)
    charms.append(charm)

charms.append(0)
prices.append(0)
nums.append(0)

for i in range(1, n + 1):
    for j in range(0, p + 1):
        for k in range(0, nums[i] + 1):
            if k * prices[i] > j:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][j-charms[i] * k] + prices[i] * k)

print(dp[n][p])
