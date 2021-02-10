'''

https://www.nowcoder.com/practice/dd0c6b26c9e541f5b935047ff4156309?tpId=37&tqId=21324&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）

本题有多组输入，请使用while(cin>>)处理

输入描述:
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述:
输出排好序的数字

示例1
输入
复制
8
1 2 4 9 3 55 64 25
0
5
1 2 3 4 5
1
输出
复制
1 2 3 4 9 25 55 64
5 4 3 2 1

'''

Inf = []
while True:
    try:
        Inf.append(input())
    except:
        break

# Inf = [
# "8",
# "1 2 4 9 3 55 64 25",
# "0",
# "5",
# "1 2 3 4 5",
# "1",
# ]

ls = []
l = []
for i, line in enumerate(Inf):
    if i % 3 == 0:
        pass
    elif i % 3 == 1:
        l = [int(_) for _ in line.split()]
    else:
        if line == "0":
            l.sort()
        else:
            l.sort(reverse=True)

        ls.append([str(_) for _ in l])

for l in ls:
    print(" ".join(l))
