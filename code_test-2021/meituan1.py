'''
小美的优美字符串
时间限制： 3000MS
内存限制： 1048576KB
题目描述：
一天，小美在写英语作业时，发现了一个十分优美的字符串：这个字符串没有任何两个字符相同。于是，小美随手写下了一个字符串，她想知道这个字符串的的所有子序列，有多少个是优美的。由于答案可能会很大，输出对20210101取模后的结果。

一个字符串的子序列定义为：原字符串删除0个或多个字符后剩下的字符保持原有顺序拼接组成的字符串为原串的子序列。如：ab是acba的子序列，但bc则不是。在本题中。空串也为原串的子序列。

两个子序列不相同，当且仅当他们对应原串的下标不相同。如aab则含有两个子序列ab。



输入描述
输入仅一行一个仅由小写字母组成的字符串。

设字符串长度为len：

1<=len<=1000000;

输出描述
输出仅包含一个正整数，表示答案对20210101取模后的结果。


样例输入
aabc
样例输出
12

提示
有下列优美的子序列：””, ”a”, “a”, “b”, “c”, “ab”, “ab”, “bc”, “ac”, “ac”, “abc”, “abc”，一共12个。

'''

string = input().strip() ## "aabc"
used = []
def dfs(i):
    if i == len(string) - 1:
        return 1
    if i >= len(string):
        return 0
    res = 0
    for c in range(i, len(string)):
        char = string[c]
        if char not in used:
            res += 1 ## char单独一个字符作为一个字符串
            used.append(char)
            res += dfs(c + 1)
            used.pop(-1)
    return res
print((dfs(0) + 1) % 20210101) ## +1是为了加上空串.
