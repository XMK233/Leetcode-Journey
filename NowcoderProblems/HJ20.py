'''
https://www.nowcoder.com/practice/184edec193864f0985ad2684fbc86841?tpId=37&tqId=21243&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有相同长度大于2的子串重复

输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG

示例1
输入
复制
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出
复制
OK
NG
NG
OK

直接暴力求解，没有闪。

'''

Inf = []
while True:
    try:
        Inf.append(input())
    except:
        break

def judgement(pw):
    ###
    if len(pw) <= 8:
        return "NG"
    ###
    types = {}
    for c in pw:
        if c >= "A" and c <= "Z":
            types["upper"] = 1
        elif c >= "a" and c <= "z":
            types["lower"] = 1
        elif c >= "0" and c <= "9":
            types["digit"] = 1
        else:
            types["special"] = 1
    if len(types) < 3:
        return "NG"
    ###
    positions = {}#collections.defaultdict(list)
    for i, c in enumerate(pw):
        # positions[c].append(i)
        if c not in positions:
            positions[c] = [i]
        else:
            for j in positions[c]: ## 对于每一个曾经出现过字符c的地方，都要做一次遍历。
                if i + 2 < len(pw) and j + 2 < len(pw) and pw[i + 1] == pw[j + 1] and pw[i + 2] == pw[j + 2]:
                    return "NG"
    ###
    return "OK"

for pw in Inf:
    print(judgement(pw))


