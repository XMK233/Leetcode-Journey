import sys

T = -1
n = -1
m = -1
a = []
b = []
c = []
res = []

### 数组a长度为n, 数组b长度为m
### c长度为n+m, 是把a, b合并起来的一个数组c.
### 问, a, b 数组里面数的顺序不乱序就能组合成c, 就打印"possible", 否则打印"not possible"
## 我的解法是暴力解法.

def judgement(n, m, a, b, c):
    c_visited = [False] * (n + m)
    ### 开始处理.
    flag = float("-inf")
    for i in range(n):
        for j in range(n + m):
            if c[j] == a[i]:  ## 这个是当前要查找的值
                if c_visited[j] == False:
                    if j > flag:
                        c_visited[j] = True
                        flag = j
                        break
                    else:
                        return False
                continue
    flag = float("-inf")
    for i in range(m):
        for j in range(n + m):
            if c[j] == b[i]:  ## 这个是当前要查找的值
                if c_visited[j] == False:
                    if j > flag:
                        c_visited[j] = True
                        flag = j
                        break
                    else:
                        return False
                continue
    return True


lines = [
    "2",
    "3 3",
    "1 2 3",
    "4 5 6",
    "1 4 2 3 5 6",
    "3 3",
    "1 2 1",
    "2 1 2",
    "1 1 1 2 2 2",
]

for i, line in enumerate(lines):
    ## print(i, line)
    if i == 0:
        T = int(line)
    elif i % 4 == 1:
        n_, m_ = line.split()
        n = int(n_)
        m = int(m_)
    elif i % 4 == 2:
        a = [int(_) for _ in line.split()]
    elif i % 4 == 3:
        b = [int(_) for _ in line.split()]
    elif i % 4 == 0:
        c = [int(_) for _ in line.split()]
        status = judgement(n, m, a, b, c)
        if status:
            res.append("possible")
        else:
            res.append("not possible")

for l in res:
    print(l)