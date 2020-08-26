lines = ["2", "2", "20 25", "40", "1", "8", "3", "3 5 100", "5 6"]
## 搜集所有的行
# lines = []
# while True:
#     try:
#         lines.append(input())
#     except:
#         break

## 每行遍历
T = 0
n = 0
groupStarts = False
getA = False
getB = False
groupCounter = 0
groups = {}

## 创建每一组的n, a, b. 然后再统一处理.
for i, line in enumerate(lines):
    ## 首行, 是组的数量
    if i == 0:
        T = int(lines[i])
        groupStarts = True
        continue
    ###
    if groupStarts:
        groupStarts = False
        groupCounter += 1
        n = int(line)
        groups[groupCounter] = {"n":n}
        getA = True
        continue
    if getA:
        getA = False
        groups[groupCounter]["a"] = [int(_) for _ in line.split()]
        if groups[groupCounter]["n"] == 1:
            getB = False
            groupStarts = True
        else:
            getB = True
        continue
    if getB:
        getB = False
        groups[groupCounter]["b"] = [int(_) for _ in line.split()]
        groupStarts = True

minutes = [] ## 其实应该是seconds.
for groupNum in groups:
    n = groups[groupNum]["n"]
    a = groups[groupNum]["a"]
    b = None
    ## 多人....排队.
    if "b" in groups[groupNum]:
        b = groups[groupNum].get("b")
        a_ = [-1] * len(a)
        # j = 1
        # i = 0
        a_[0] = a[0]

        for i in range(len(b)):
            for j in range(i + 1, len(a)):
                if j == i + 1:
                    if j == 1:
                        a_[j] = min(a[j] + a[j - 1], b[i])
                    else:
                        a_[j] = min(a_[j - 2] + b[i], a_[j - 1] + a[j])
                else:
                    a_[j] = a_[j - 1] + a[j]
        minutes.append(a_[-1])
    ## 一人我排队醉
    else:
        minutes.append(a[0])

print(minutes)