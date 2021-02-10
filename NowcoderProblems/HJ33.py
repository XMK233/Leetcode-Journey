'''
https://www.nowcoder.com/practice/66ca0e28f90c42a196afd78cc9c496ea?tpId=37&tqId=21256&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

本题含有多组输入用例，每组用例需要你将一个ip地址转换为整数、将一个整数转换为ip地址。



输入描述:
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述:
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

示例1
输入
复制
10.0.3.193
167969729
输出
复制
167773121
10.3.3.193

暴力解法。

'''

Inf = []
while True:
    try:
        Inf.append(input())
    except:
        break

def transform2Digits(ip):
    finalString = ""
    for i in ip.split("."):
        part = str(bin(int(i)))[2:]
        finalString += (8 - len(part)) * "0" + part
    return int(finalString, 2)

def transform2Ip(digits):
    part = str(bin(int(digits)))[2:]
    newStr = (32 - len(part)) * "0" + part
    l = []
    for i in range(0, 32, 8):
        l.append(str(int(newStr[i:i+8], 2)))
    return ".".join(l) # str(bin(int(digits)))

def transform(string):
    if "." in string:
        return transform2Digits(string)
    else:
        return transform2Ip(string)

for string in Inf:
    print(transform(string))