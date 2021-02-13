'''
https://www.nowcoder.com/practice/22948c2cad484e0291350abad86136c3?tpId=37&tqId=21331&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数。

示例1
输入
复制
5 7
输出
复制
35

记住算法的最核心原理是: 两数乘积除以最大公约数

'''

num1, num2 = map(int, input().split())

def getGreatestCommonDivisor(num1, num2):
    while True:
        quotient, mod = divmod(num1, num2)
        if mod == 0:
            return num2
        else:
            num1 = num2
            num2 = mod

if num1 < num2:
    num1, num2 = num2, num1

print(num1 * num2 // getGreatestCommonDivisor(num1, num2))