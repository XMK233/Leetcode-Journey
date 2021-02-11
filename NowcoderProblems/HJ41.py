'''
https://www.nowcoder.com/practice/f9a4c19050fc477e9e27eb75f3bfd49c?tpId=37&tqId=21264&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；
每种砝码对应的数量为x1,x2,x3...xn。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。


注：

称重重量包括0


输入描述:
输入包含多组测试数据。

对于每组测试数据：

第一行：n --- 砝码数(范围[1,10])

第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])

第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
输出描述:
利用给定的砝码可以称出的不同的重量数

示例1
输入
复制
2
1 2
2 1
输出
复制
5

'''

# -*- coding:utf-8 -*-
res = []
while True:
    try:
        n = int(input())
        m = list(map(int, input().split()))  # python3这块没有python2来的直接，需要用list转换一下
        x = list(map(int, input().split()))

        totalWeight = 0
        for mi, xi in zip(m, x):
            totalWeight += mi * xi

        l = [0] * (totalWeight + 1)  ## l[i]指的是，重量i能否被凑出来。
        l[0] = 1  ## l[0]必为1，说明重量0必能凑出来。
        for mi, xi in zip(m, x):  ## 这层循环指的是啥？增加了一种砝码（mi）若干个（xi）。
            l_new = l.copy()  ## 这里是复制一份数组，每一轮都保存一个l的镜像，遍历的时候看l，更新的时候更新镜像，然后将l替换为镜像即可。
            for n in range(1, xi + 1):  ## n就是指mi砝码用n个的情况。
                newWeight = mi * n  ## 新增砝码的重量
                for i in range(0, len(l)):
                    if l[i] > 0:  ## 这里遍历l。l[i]>0意味着之前有砝码组合能够凑出i的重量。
                        l_new[i + newWeight] = 1  ## 只要之前的砝码能够凑出某重量，那么这个重量i加上新增重量weight-->(i+newWeight)也能够凑出来。就要标记一下
                    else:
                        pass
            l = l_new

        # print(sum(l))## 标记过的地方就是1了，所以数能凑出来的重量，只要直接计算sum就行了。
        res.append(sum(l))
    except:
        break

for i in res:
    print(i)

## 以下为参考方法。

# while True:
#     try:
#         n=int(input())
#         m=list(map(int,input().split()))#python3这块没有python2来的直接，需要用list转换一下
#         x=list(map(int,input().split()))
#         diff={0}
#         for i in range(n):
#             d=diff.copy()
#             for j in range(x[i]):
#                 for k in d:
#                     temp=k+m[i]*(j+1)
#                     if temp not in d:
#                         diff.add(temp)
#         print(len(diff))
#     except:
#         break