'''
https://www.nowcoder.com/questionTerminal/7f4be54b37a04fdaa4ee545819151114

链接：https://www.nowcoder.com/questionTerminal/7f4be54b37a04fdaa4ee545819151114
来源：牛客网

输入一个整数n(2<=n<=10000)，要求输出所有从1到这个整数之间(不包括1和这个整数)个位为1的素数，如果没有则输出-1。

输入描述:
输入有多组数据。
每组一行，输入n。


输出描述:
输出所有从1到这个整数之间(不包括1和这个整数)个位为1的素数(素数之间用空格隔开，最后一个素数后面没有空格)，如果没有则输出-1。
示例1
输入
100
输出
11 31 41 61 71

'''
def getAllPrimeNumbers(n):
    i = 2
    nums = [0] * (n + 1)
    traverseUpLimit = pow(n, 0.5)
    while i <= traverseUpLimit:
        if nums[i] == 0: ## 没有被筛掉的数字
            for j in range(i + 1, n + 1):
                if j % i == 0:
                    nums[j] = 1
        i += 1

    res = []
    for i in range(2, len(nums)):
        if nums[i] == 0 and (i - 1) % 10 == 0 and i != n: ## 素数, 且个位为1, 且不为这个数
            res.append(str(i))
    return res

finalRes = []
while True:
    try:
        finalRes.append(getAllPrimeNumbers(int(input())))
    except:
        break

for fr in finalRes:
    print(" ".join(fr))


