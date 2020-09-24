## 走迷宫.
## 迷宫的原来的地形是未知的. 然后一个小人, 从起点开始, 一次一次地探索, 比如尝试往上走, 发现走得了, 就继续走;
## 走不了, 就回头.
## 直到终点.
## 然后, 把这个小人探路的过程总结下来. 0, 1, 2, 3分别代表上下左右; 1代表可走, -1反之.
## 请问, 在一定有路到终点的情况下, 已知上述探路过程记录, 请问从起点到终点的最短路径有多长.

### 我的思路其实很简单, 就是先构建一个棋盘, 然后标记上起点位置、终点位置、是否能走。
### 然后从起点出发，进行一波dfs。
### 但很可惜，样例能过，但是最终accept了0个测试用例。白做。tnd。

def inEachGroup(steps):
    directionMax = {
        "up": 0,
        "down": 0,
        "left": 0,
        "right": 0
    }
    directionCur = {
        "vertical": 0,
        "horizontal": 0
    }
    for step in steps:
        direction, successful = step[0], step[1]
        if successful == -1:
            continue
        if direction == 0:
            directionCur["vertical"] += 1
            # if directionCur["vertical"] >= 0 and directionCur["vertical"] > directionMax["up"]:
            #     directionMax["up"] = directionCur["vertical"]
            if directionCur["vertical"] >= 0:
                directionMax["up"] = max(directionCur["vertical"], directionMax["up"])
        elif direction == 1:
            directionCur["vertical"] -= 1
            if directionCur["vertical"] < 0:
                directionMax["down"] = max(abs(directionCur["vertical"]), directionMax["down"])
        elif direction == 2:
            directionCur["horizontal"] -= 1
            if directionCur["horizontal"] < 0:
                directionMax["left"] = max(abs(directionCur["horizontal"]), directionMax["left"])
        elif direction == 3:
            directionCur["horizontal"] += 1
            if directionCur["horizontal"] >= 0:
                directionMax["right"] = max(directionCur["horizontal"], directionMax["right"])
    #################
    numRow = directionMax["up"] + directionMax["down"] + 1
    numCol = directionMax["left"] + directionMax["right"] + 1
    plate = [[0] * numCol for i in range(numRow)]
    startRow, startCol = directionMax["up"], directionMax["left"]
    ##################
    curRow, curCol = startRow, startCol
    plate[curRow][curCol] = 1
    for step in steps:
        direction, successful = step[0], step[1]
        if successful == -1:
            continue
        if direction == 0:
            curRow -= 1
            plate[curRow][curCol] = 1
        elif direction == 1:
            curRow += 1
            plate[curRow][curCol] = 1
        elif direction == 2:
            curCol -= 1
            plate[curRow][curCol] = 1
        elif direction == 3:
            curCol += 1
            plate[curRow][curCol] = 1
    targetRow, targetCol = curRow, curCol
    ###################
    # print((startRow, startCol), (targetRow, targetCol))
    # print(plate)
    # disMatrix = [[float("Inf")] * numCol for i in range(numRow)]
    # disMatrix[targetRow][targetCol] = 0
    visited = [[False] * numCol for i in range(numRow)]
    visited[startRow][startCol] = True
    ##
    def dfs(plate, visited, startRow, startCol, numRow, numCol, targetRow, targetCol):
        minDistance = float("Inf")
        for d in ds:
            nextRow, nextCol = startRow + d[0], startCol + d[1]
            if nextRow >= 0 and nextRow < numRow and nextCol >= 0 and nextCol < numCol and plate[nextRow][
                nextCol] == 1 and visited[nextRow][nextCol] == False:  ## 能走的话...
                # if disMatrix[nextRow][nextCol] != float("Inf"):
                #     minDistance = min(minDistance, disMatrix[nextRow][nextCol] + 1)
                # else:
                if nextRow == targetRow and nextCol == targetCol:
                    return 1
                else:
                    visited[nextRow][nextCol] = True
                    distance = dfs(plate, visited, nextRow, nextCol, numRow, numCol, targetRow, targetCol) + 1
                    minDistance = min(minDistance, distance)
                    # visited[nextRow][nextCol] = False
            else:
                continue
        # disMatrix[startRow][startCol] = minDistance
        return minDistance
    ##
    return dfs(plate, visited, startRow, startCol, numRow, numCol, targetRow, targetCol)
ds = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]
T = int(input())
res = []
for t in range(T):
    N = int(input())
    steps = []
    for n in range(N):
        step = [int(_) for _ in input().split()]
        steps.append(step)
    res.append(inEachGroup(steps))
for r in res:
    print(r)

# steps1 = [
# [0, 1],
# [0, -1],
# [1, 1],
# [1, 1],
# [1, -1],
# [0, 1],
# [2, 1],
# [2, -1],
# [3, 1],
# [3, 1],
#  ]
#
# steps2 = [
#     [0, 1],
#     [0, 1],
# [3, 1],
# [3, 1],
# [1, 1],
# [1, 1],
# [2, 1],
# [0, 1],
# ]
################################################################

def inEachGroup(steps):
    directionMax = {
        "up": 0,
        "down": 0,
        "left": 0,
        "right": 0
    }
    directionCur = {
        "vertical": 0,
        "horizontal": 0
    }
    for step in steps:
        direction, successful = step[0], step[1]
        if successful == -1:
            continue
        if direction == 0:
            directionCur["vertical"] += 1
            # if directionCur["vertical"] >= 0 and directionCur["vertical"] > directionMax["up"]:
            #     directionMax["up"] = directionCur["vertical"]
            if directionCur["vertical"] >= 0:
                directionMax["up"] = max(directionCur["vertical"], directionMax["up"])
        elif direction == 1:
            directionCur["vertical"] -= 1
            if directionCur["vertical"] < 0:
                directionMax["down"] = max(abs(directionCur["vertical"]), directionMax["down"])
        elif direction == 2:
            directionCur["horizontal"] -= 1
            if directionCur["horizontal"] < 0:
                directionMax["left"] = max(abs(directionCur["horizontal"]), directionMax["left"])
        elif direction == 3:
            directionCur["horizontal"] += 1
            if directionCur["horizontal"] >= 0:
                directionMax["right"] = max(directionCur["horizontal"], directionMax["right"])
    #################
    numRow = directionMax["up"] + directionMax["down"] + 1
    numCol = directionMax["left"] + directionMax["right"] + 1
    plate = [[0] * numCol for i in range(numRow)]
    startRow, startCol = directionMax["up"], directionMax["left"]
    ##################
    curRow, curCol = startRow, startCol
    plate[curRow][curCol] = 1
    for step in steps:
        direction, successful = step[0], step[1]
        if successful == -1:
            continue
        if direction == 0:
            curRow -= 1
            plate[curRow][curCol] = 1
        elif direction == 1:
            curRow += 1
            plate[curRow][curCol] = 1
        elif direction == 2:
            curCol -= 1
            plate[curRow][curCol] = 1
        elif direction == 3:
            curCol += 1
            plate[curRow][curCol] = 1
    targetRow, targetCol = curRow, curCol
    ###################
    # print((startRow, startCol), (targetRow, targetCol))
    # print(plate)
    # disMatrix = [[float("Inf")] * numCol for i in range(numRow)]
    # disMatrix[targetRow][targetCol] = 0
    visited = [[False] * numCol for i in range(numRow)]
    visited[startRow][startCol] = True
    ##
    def dfs(plate, visited, startRow, startCol, numRow, numCol, targetRow, targetCol):
        minDistance = float("Inf")
        for d in ds:
            nextRow, nextCol = startRow + d[0], startCol + d[1]
            if nextRow >= 0 and nextRow < numRow and nextCol >= 0 and nextCol < numCol and plate[nextRow][
                nextCol] == 1 and visited[nextRow][nextCol] == False:  ## 能走的话...
                # if disMatrix[nextRow][nextCol] != float("Inf"):
                #     minDistance = min(minDistance, disMatrix[nextRow][nextCol] + 1)
                # else:
                if nextRow == targetRow and nextCol == targetCol:
                    return 1
                else:
                    visited[nextRow][nextCol] = True
                    distance = dfs(plate, visited, nextRow, nextCol, numRow, numCol, targetRow, targetCol) + 1
                    minDistance = min(minDistance, distance)
                    visited[nextRow][nextCol] = False
            else:
                continue
        # disMatrix[startRow][startCol] = minDistance
        return minDistance
    ##
    return dfs(plate, visited, startRow, startCol, numRow, numCol, targetRow, targetCol)



# minDis = inEachGroup(steps2)
# print(minDis)