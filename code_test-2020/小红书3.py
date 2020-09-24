"""
航海士们在获得海贼王的宝藏后，起帆回家。为了能尽快回到家中，每天白天他们必须航行至少L海里，但船的速度又只能最多支持他们航行T海里，晚上大家会停船休息。夜晚的大海是充满危险的，在航线上大家知道有一些危险区域的存在，它们分别距离起点Ai海里，大家希望晚上尽量不在这些区域休息。

为了简化问题，我们假设航线是一条直线，船每天航行的距离是整数海里。现在，请帮大家规划一个航行方案，使得到达终点前在危险区域休息的次数最少。
"""

X = int(input())
L, T, N = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
A.sort()
###########################
# X = 10
# L, T, N = 2, 3, 4
# A = [2, 3, 5, 6]
###########################
# A.insert(0, 0)## 起点位置
# M = [i for i in range(X + 1)]
def helper(start):
    ### 走最少距离能到的地方
    possibility_min = start + L
    ### 走最大距离能到的地方
    possibility_max = start + T
    ### 如果最少能走到的地方已经大于了最后一个危险区, 或者已经到达终点:
    if possibility_min > A[-1] or possibility_min >= X:
        return 0
    ### 记录危险区域
    dangerous = float("Inf")
    for possibility in range(possibility_min, possibility_max + 1):
        if possibility in A: ## 夜宿危险区
            dangerous = min(1 + helper(possibility), dangerous)
        else: ## 夜宿安全区
            dangerous = min(helper(possibility), dangerous)
    return dangerous

print(helper(0))
