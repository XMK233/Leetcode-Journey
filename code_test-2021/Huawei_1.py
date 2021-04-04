# inputLines = []
# while True:
#     try:
#         inputLines.append(input())
#     except:
#         break
#
# #############################
numLines = int(input())
lines = []
for nl in range(numLines):
    lines.append(input())
########################
# numLines = 5
# lines = [
# "ZhangSan married 10 50",
# "Jimmy unmarried 10 50",
# "WangWu unmarried 15 60",
# "LiSi unmarried 1 30",
# "Amy unmarried 1 30",
# ]
############################
## 其实本题的意思就是，根据每一个line的四个元素分别进行排序。有点像sql里面的orderby
data = [
    line.split() for line in lines
]

for d in data:
    if d[1] == "unmarried":
        d[1] = 0
    else:
        d[1] = 1
    d[2] = int(d[2])
    d[3] = int(d[3])

data.sort(key=lambda x: (x[3], x[2], x[1], x[0]), reverse=True)

import collections
keyOrder = []
keyWorkers = collections.defaultdict(list)
for d in data:
    key = (d[1], d[2], d[3])
    if key not in keyOrder:
        keyOrder.append(key)
    keyWorkers[key].append(d[0])
for key in keyOrder:
    names = sorted(keyWorkers[key])
    for name in names:
        print(name)