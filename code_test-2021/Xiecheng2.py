'''

果盘组合
时间限制： 3000MS
内存限制： 589824KB
题目描述：
水果店有不同种的果盘组合，比如3个苹果1个梨、2个苹果3个梨等等。

请你选择尽可能多的果盘组合，要求最多只能有m个苹果、n个梨。

其中：果盘组合由字符串表示，"a"表示苹果、"p"表示梨；果盘不可重复选择



输入描述
一共有5个果盘，分别为a,ppap,ap,aaappa,p。限制最多取2个苹果，3个梨

输出描述
满足最多2个苹果、3个梨的最大选择为"a", "ap", "p"，因此答案为3


样例输入
a,ppap,ap,aaappa,p 2 3
样例输出
3

提示
样例解析: 一共提供了5个果盘。满足最多2个苹果、3个梨的最大选择为"a", "ap", "p"，因此答案为3。

'''
s = "a,ppap,ap,aaappa,p 2 3" #input()#.split()
l = s.split()
plates, requirements = l[0].split(","), l[-2:]
plates.insert(0, "#")

remnants = [[2, 3]]
dp = [0]
for i in range(1, len(plates)):
    numA = plates[i].count("a")
    numP = plates[i].count("p")
    maxIndex = -1
    for j in range(len(remnants) - 1, -1, -1):
        if remnants[j][0] >= numA and remnants[j][1] >= numP:
            maxIndex = j
            break
            # remnants.append([remnants[j][0] - numA, remnants[j][1], numP])
            # dp.append(dp[j] + 1)
    if maxIndex < 0:
        remnants.append(remnants[-1])
        dp.append(dp[-1])
    else:
        if dp[maxIndex] + 1 >= dp[-1]:
            remnants.append(
                [remnants[maxIndex][0] - numA, remnants[maxIndex][1] - numP]
            )
            dp.append(dp[maxIndex] + 1)
        else:
            remnants.append(remnants[-1])
            dp.append(dp[-1])

print(remnants)
print(dp)
print(dp[-1])

# import collections
# s = "2 3" #input()#.split()
#
# # print(plates)
# # print(requirements)
# def judge(s):
#     if not ("a" in s and "p" in s):
#         return 0
#     l = s.split()
#     if len(l) < 3:
#         return 0
#     plates, requirements = l[0].split(","), l[-2:]
#     requirements = [int(_) for _ in requirements]
#     res = 0
#     dupPlates = {}
#     for plate in plates:
#         # dupPlates[plate] = 1
#         # if len(plate) >= sum(requirements):
#         #     continue
#         count = collections.defaultdict(int)
#         for fruit in plate:
#             count[fruit] += 1
#         if count["a"] < requirements[0] and count["p"] < requirements[1]:
#            res += 1
#     return res
#
# print(judge(s))