'''
时间限制： 3000MS
内存限制： 589824KB
题目描述：
很久很久以前，乡村里住着一个老农。有一天他打算修葺屋顶横梁。老农仓库里放着一排长度不一样的木材，我们知道每个木材的长度。当然在很久很久以前，度量衡没有那么精确。所以我们的木材长度都是诸如3米，2米，5米和1米等等这种。为了方便起见，老农打算从仓库里取出几根挨在一起的木材连接在一起作为新的横梁。写一个算法，计算老农有几种取法。



输入描述
Input1=木材长度列表

6,2,5,5,3,7,3,1,1,4,4,8,8

Input2=横梁长度

10

输出描述
方案数目

4


样例输入
6,2,5,5,3,7,3,1,1,4,4,8,8,1,1,5,4
10
样例输出
6
'''
logLens = [int(_) for _ in input().strip().split(",")]
targetLen = int(input().strip())
def hengLiangLength(logLens, targetLen):
    record = {targetLen: 1}
    total = 0
    res = 0
    for logLen in logLens:
        total += logLen
        tmp = 0
        if total in record:
            tmp = record[total]
        res += tmp
        newLen = total + targetLen
        if newLen in record:
            record[newLen] = record[newLen] + 1
        else:
            record[newLen] = 1
    # print(record)
    return res
print(hengLiangLength(logLens, targetLen))