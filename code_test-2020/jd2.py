## AC了

def oneGroup(n, m, myMap):
    visited = [[False] * m for _ in range(n)]
    #########
    endLoop = False
    princePlace = None
    for i in range(n):
        for j in range(m):
            if myMap[i][j] == "S":
                princePlace = (i, j)
                endLoop = True
        if endLoop:
            break
    #########
    endLoop = False
    princessPlace = None
    for i in range(n):
        for j in range(m):
            if myMap[i][j] == "E":
                princessPlace = (i, j)
                endLoop = True
        if endLoop:
            break
    #########
    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    #########
    def canGo(visited, curPlace):
        ###
        if curPlace == princessPlace:
            return True
        ###
        # mark = False
        for d in directions:
            nextPlace = (curPlace[0] + d[0], curPlace[1] + d[1])
            ## 首先判断有无出界
            if not (nextPlace[0] < n and nextPlace[0] >= 0 and nextPlace[1] < m and nextPlace[1] >= 0):
                continue
            ## 然后判断下一个地方是否是障碍物
            if myMap[nextPlace[0]][nextPlace[1]] == "#" or visited[nextPlace[0]][nextPlace[1]] == True:
                continue
            visited[curPlace[0]][curPlace[1]] = True
            result = canGo(visited, nextPlace)
            if result == True:
                return True
            # mark = canGo(visited, nextPlace) or mark
            visited[curPlace[0]][curPlace[1]] = False
        return False

    if canGo(visited, princePlace):
        return "YES"
    else:
        return "NO"
####
#############
# n = 2
# m = 2
#
# myMap = [
#     "#E",#[".", "E"],
#     "S#"#["S", "."]
# ]
##########################
numOfGroup = int(input())
res = []
for g in range(numOfGroup):
    n, m = [int(_) for _ in input().split()]
    myMap = []
    for line in range(n):
        myMap.append(input())
    res.append(oneGroup(n, m, myMap))
for r in res:
    print(r)