import collections
bridgeCost = {}
neighbor = collections.defaultdict(list)
def dfs(bridgeCost, neighbor, start, target, visited):
    if start == target:
        return 0
    minCost = float("Inf")
    allVisited = True
    for end in neighbor[start]:
        if visited[int(end) - 1]:
            continue
        allVisited = False
        visited[int(start) - 1] = True
        currentCost = bridgeCost["{} {}".format(start, end)] if "{} {}".format(start, end) in bridgeCost else bridgeCost["{} {}".format(end, start)]
        minCost = min(minCost, currentCost + dfs(bridgeCost, neighbor, end, target, visited))
        visited[int(start) - 1] = False
    return 0 if allVisited else minCost
###############################
# n, m = [int(s) for s in input().split()]
# for i in range(m):
#     u, v, _ = input().split()
#     period = int(_)
#     neighbor[u].append(v)
#     neighbor[v].append(u)
#     bridgeCost["{} {}".format(u, v)] = period
#     bridgeCost["{} {}".format(v, u)] = period
# start, Paris, startDate = input().split()
##################################
n, m = 4, 4
inputLines = [
    "1 2 25",
"1 3 18",
"2 4 28",
"3 4 22",
]
for inputLine in inputLines:
    u, v, _ = inputLine.split()
    period = int(_)
    neighbor[u].append(v)
    neighbor[v].append(u)
    bridgeCost["{} {}".format(u, v)] = period
    bridgeCost["{} {}".format(v, u)] = period
start, Paris, startDate = "1", "4", "7.9/8"
##############
visited = [0] * n
deltime = dfs(bridgeCost, neighbor, start, Paris, visited)
### 下面这部分, 没写出来. 太遗憾了. 哎. 早知道第一题就不做了. 第一题是连通图最小权重计算. 狗日的.
import datetime
d = datetime.datetime.strptime(startDate, "%m.%d/%H")
d2 = d + datetime.timedelta(hours=deltime)
d2s = d2.strftime("%m.%d/%H")
month = d2s.split(".")[0]
day, hour = d2s.split(".")[1].split("/")
print("{}.{}/{}".format(int(month), int(day), int(hour)))