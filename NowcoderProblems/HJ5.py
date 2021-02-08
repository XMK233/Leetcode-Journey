# 作者：商君
# 链接：https://www.nowcoder.com/discuss/397018?type=1
# 来源：牛客网

# 题目描述
# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
#
# 输入描述:
# 输入一个十六进制的数值字符串。注意：一个用例会同时有多组输入数据，请参考帖子https://www.nowcoder.com/discuss/276处理多组输入的问题。
#
# 输出描述:
# 输出该数值的十进制字符串。不同组的测试用例用\n隔开。
#
# 示例1
# 输入
# 复制
# 0xA
# 0xAA
# 输出
# 复制
# 10
# 170

'''
方法很赖皮, 就是直接用python自带的进制转换. 技巧是int(string, <string的原进制>) ==> 10进制的数字.
'''

Inf = []
while True:
    try:
        Inf.append(list(input().split()))
    except:
        break



for words in Inf:
    string = words[0]
    newStr = string.replace("0x", "")
    print(int(newStr, 16))