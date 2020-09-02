## 方阵.
### 如果维数是奇数的话, 就画一个米字型, 米字是由0组成的.
### 如果是偶数, 就画一个叉.
## 然后呢, 米字和x字的线的中间部分, 填上数字1到8.
## 我的程序AC了, 你试试不同的n就可以看到例子了.
n = 7

matrix = [["0"] * n for _ in range(n)]
if n % 2 == 0:
    for i in range(0, n//2-1):
        for j in range(n):
            if i < j and i + j < n - 1:
            # if i == j or i + j == n-1:
            #     continue
            # else:
            #     if i < j:
                if j < n//2:
                    matrix[i][j] = "2"
                else:
                    matrix[i][j] = "1"
    for i in range(n//2 + 1, n):
        for j in range(n):
            if i + j >= n and i + j < 2 * i:
                if j < n//2:
                    matrix[i][j] = "5"
                else:
                    matrix[i][j] = "6"
    ###
    for i in range(0, n//2-1):
        for j in range(n):
            if i < j and i + j < n - 1:
            # if i == j or i + j == n-1:
            #     continue
            # else:
            #     if i < j:
                if j < n//2:
                    matrix[j][i] = "3"
                else:
                    matrix[j][i] = "4"
    for i in range(n//2 + 1, n):
        for j in range(n):
            if i + j >= n and i + j < 2 * i:
                if j < n//2:
                    matrix[j][i] = "8"
                else:
                    matrix[j][i] = "7"
else:
    for i in range(0, n//2-1):
        for j in range(n):
            if i < j and i + j < n - 1:
            # if i == j or i + j == n-1:
            #     continue
            # else:
            #     if i < j:
                if j < n//2:
                    matrix[i][j] = "2"
                elif j > n//2:
                    matrix[i][j] = "1"
    for i in range(n//2 + 1, n):
        for j in range(n):
            if i + j >= n and i + j < 2 * i:
                if j < n//2:
                    matrix[i][j] = "5"
                elif j > n//2:
                    matrix[i][j] = "6"
    ###
    for i in range(0, n//2-1):
        for j in range(n):
            if i < j and i + j < n - 1:
            # if i == j or i + j == n-1:
            #     continue
            # else:
            #     if i < j:
                if j < n//2:
                    matrix[j][i] = "3"
                elif j > n//2:
                    matrix[j][i] = "4"
    for i in range(n//2 + 1, n):
        for j in range(n):
            if i + j >= n and i + j < 2 * i:
                if j < n//2:
                    matrix[j][i] = "8"
                elif j > n//2:
                    matrix[j][i] = "7"

for line in matrix:
    print(" ".join(line))

