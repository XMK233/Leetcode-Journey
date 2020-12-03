## lines每一行这样理解：A1号车，从1号点出发，目的地50号点，它在1号点的时候速度是49KM/H。这每一行line是一条车辆状态记录。
## 然后，任何一辆车经过某一个点的时候，速度都变成那个点的速度，此后，除非遇到另一个节点，速度保持不变。
## 如果车辆状态记录在某一个点有好几条，那怎么确定这个点的速度呢？求平均速度就好了。
## 然后问，每一辆车从起点到目的地总共需要多久。单位分钟。

lines = [
    "A1 1 49 50",
    "B5 21 40 45"
]

carOrder = []
startTarget = {}
targetMax = -1
import collections
posVDict_origin = collections.defaultdict(list)
posVDict_avg = {}

resDict = {}

for line in lines:
    carNum, _1, _2, _3 = line.split()
    position, speed, target = int(_1), int(_2), int(_3)
    # cars.append(carNum)
    # print(carNum, position, speed, target)
    ## 最远距离
    if target > targetMax:
        targetMax = target
    ## posVDict_origin
    posVDict_origin[position].append(speed)
    startTarget[carNum] = [position, target]
    resDict[carNum] = 0
    carOrder.append(carNum)

for key, values in posVDict_origin.items():
    posVDict_avg[key] = sum(values)/len(values)
# print(posVDict_avg)

positions = list(posVDict_avg.keys())
positions.sort()
positions.append(targetMax + 1)
for i in range(0, len(positions) - 1):
    # print(positions[i], positions[i+1])
    for j in range(positions[i], positions[i+1]):
        posVDict_avg[j] = posVDict_avg[positions[i]]
# print(posVDict_avg)

for carNum, journey in startTarget.items():
    start, target = journey[0], journey[-1]
    flagPos = start
    flagSpeed = posVDict_avg[start]
    for i in range(start, target):
        if posVDict_avg[i] != flagSpeed:
            resDict[carNum] += (i - flagPos) / flagSpeed
            flagPos = i
            flagSpeed = posVDict_avg[i]
    resDict[carNum] += (target - flagPos + 1)/flagSpeed
    resDict[carNum] = round(resDict[carNum] * 60)

for carNum in carOrder:
    print("{} {}".format(carNum, resDict[carNum]))
