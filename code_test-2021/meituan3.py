'''
小美的讨厌数字
时间限制： 4000MS
内存限制： 589824KB
题目描述：
小美发明了一个函数：f(x)，表示将x的所有正整数因子提取出来之后从小到大排列，再将数字拼接之后得到的数字串。例如：10的所有因子为1,2,5,10，那么将这些因子从小到大排序之后再拼接得到的数字串为12510，即f(10)=12510。

小美十分讨厌数字k，如果f(x)中含有某个子串对应的数字等于k，那么她的不高兴度就会增加1。例如：f(8)=1248，那么其所有的子串为：1,2,4,8,12,24,48,124,248,1248，只要k等于其中任意一个值，那么小美的不高兴度就会增加1。对于每一个数，其不高兴度至多增加1。

现在，有一个长度为n的正整数序列，定义其不高兴度为序列中所有数的不高兴度的总和。小美想要知道自己对于这个序列的总不高兴度为多少。



输入描述
第一行两个正整数n,k；

第二行n个正整数ai，表示该序列。

1≤n≤105，1≤k，ai≤2x104

输出描述
输出一行一个正整数，表示小美的总不高兴度。


样例输入
5 13
13 31 10 9 20
样例输出
3

提示
f(13)=113,含有13；
f(31)=131,含有13；
f(10)=12510,不含有13；
f(9)=139，含有13；
f(20)=12451020,不含有13。
综上，不高兴度为3。

这题没提交. 下面的做法不保证对. 所以整个就薛定谔了.
'''
n, k = 5, 13#[int(_) for _ in input().strip().split()]
nums = [13, 31, 10, 9, 20]##[int(_) for _ in input().strip().split()]
def allFactor(n):
    if n == 0: return [0]
    if n == 1: return [1]
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res
def subStrs(s):
    res = []
    for x in range(len(s)):
        for i in range(len(s) - x):
            res.append(s[i:i + x + 1])
    return res
res = 0
for num in nums:
    newStr = "".join([str(k) for k in allFactor(num)])
    subStrings = subStrs(newStr)
    for subString in subStrings:
        if int(subString) == k:
            res += 1
            break
print(res)
