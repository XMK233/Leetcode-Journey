import collections
numGroup = int(input())
res = []

def dfs(bridgeCost, neighbor, start, visited):
    minCost = float("Inf")
    allVisited = True
    for end in neighbor[start]:
        if visited[int(end)]:
            continue
        allVisited = False
        visited[int(start)] = True
        currentCost = bridgeCost["{} {}".format(start, end)] if "{} {}".format(start, end) in bridgeCost else bridgeCost["{} {}".format(end, start)]
        minCost = min(minCost, currentCost + dfs(bridgeCost, neighbor, end, visited))
        visited = False
    return 0 if allVisited else minCost


for _ in range(numGroup):
    n, m, k = [int(s) for s in input().split()] ## n是岛的数量, k是预算.
    bridgeCost = {}
    neighbor = collections.defaultdict(list)
    for i in m: ## m是记录条数.
        island1, island2, cost = input().split()
        cost = int(cost)
        neighbor[island1].append(island2)
        neighbor[island2].append(island1)
        bridgeCost["{} {}".format(island1, island2)] = cost
        bridgeCost["{} {}".format(island2, island1)] = cost
    visited = [0] * n
    print(dfs(bridgeCost, neighbor, 1, visited))

