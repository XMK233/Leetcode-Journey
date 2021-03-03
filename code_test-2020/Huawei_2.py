# S = input()
# P = input()
#####################
S = "ABBCCCBCCAA"
P = ""
##################
## 就是说，往P字符串里面一次插入大等于3个的某字符，然后插入多次，问能否组成S字符串。
## 本题没做出来。我尝试用堆栈解有效括号的思路去解。
## 如果P是空串，或者是P的字符在S中从未出现过，那倒是还能做。
## 但如果P中的字符是S中出现过的，那就不好办了。所以这也就是我GG的地方。

def getRes(S, P):
    ## 首先第一步,把p化为不是由字母构成的字符串. 比如转为数字.
    ps = list(P)
    ps1 = [
        str(ord(c)) for c in ps
    ]
    # print(ps1)
    ## 第二步, 遍历S字符串
    res = 0
    stack = []
    ss = list(S)
    i = 0
    while i < len(S):
        c = S[i]
    # for c in ss:
        if len(stack) == 0:
            stack.append([c])
        else:
            if c != stack[-1][0]:
                if len(stack[-1]) >= 3:
                    stack.pop(-1)
                    res += 1
                    continue
                else:
                    # return -1
                    pass
                stack.append([c])
            else:
                stack[-1].append(c)
                # if len(stack[-1]) >= 3:
        i += 1
    if len(stack) > 0:
        if len(stack[-1]) >= 3:
            stack.pop(-1)
            res += 1
    # print(stack)
    if len(stack) != len(ps1):
        return -1
    return res

print(getRes(S, P))