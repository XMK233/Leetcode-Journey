## 字符串是指出故障的记录. f就是出故障, n就是没故障, x就保持与上一次一样的状态.
## 如果连续N次出故障, 或者在连续的M次里面总计有T次出故障, 就报一个真·出故障状态。
## 最终返回：从第一次爆出真·出故障状态以来，直到故障被消掉以来，总共真·出故障状态能持续多久。
## 怎么消掉故障？连续P次没有出故障。

lines = [
    "10 4 3 3",
    "fnfnfnffxfnnnnn"
]
# "3 10 6 3",
# "nffnffnffnffnnnnn"
# 6
## #8
#
# "3 10 6 3"
# nffnffffffnnnnn
# 6
## #6
#
# 10 4 3 3
# fnfnfnffxfnnnnn
# 5
## #7
#
# 10 4 3 3
# fxffnfnffnfnnnnn
# 10
## #3



N, M, T, P = -1, -1, -1, -1
for i, line in enumerate(lines):
    if i == 0:
        N, M, T, P = [int(_) for _ in line.split()]
status = lines[-1]
print(N, M, T, P, status)

n, m, t, p = N, M, T, P

consequtiveAlertIndex = len(status)
for i in range(len(status)):
    if status[i] == "f":
        n -= 1
    else:
        n = N
    if n == 0:
        consequtiveAlertIndex = i
# print(consequtiveAlertIndex)

totalAlertIndex = len(status)
headIndex = 0
tailIndex = M - 1
flag_earlyFound = False
for i in range(0, M):
    if status[i] == "f":
        t -= 1
    if t == 0:
        totalAlertIndex = i
        flag_earlyFound = True
        break
if not flag_earlyFound:
    while tailIndex < len(status):
        tailIndex += 1
        headIndex += 1
        ##
        if status[tailIndex] == "f":
            t -= 1
        ##
        # if status[tailIndex-1] == "n" and status[tailIndex] == "f":
        #     t += 1
        if status[headIndex-1] == "f" and status[headIndex] == "n":
            t += 1
        if t == 0:
            totalAlertIndex = tailIndex
            break

earliestAlertPosition = min(consequtiveAlertIndex, totalAlertIndex)
# print(earliestAlertPosition)
alerted = True
exceedStatus = True
for i in range(earliestAlertPosition, len(status)):
    if i == earliestAlertPosition:
        pass
    ##
    if status[i] == "n":
        p -= 1
    elif status[i] == "x":
        if alerted:
            p = P
        else:
            p -= 1
    else:
        p = P
    ##
    if p == 0:
        print(i - earliestAlertPosition)
        exceedStatus = False
        break

if exceedStatus:
    print(len(status) - earliestAlertPosition)

