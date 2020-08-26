n = 4

def getV(n):
    if n == 1:
        return 1
    else:
        return n * getV(n - 1)
def combination(n, m):
    if n == m:
        return 1
    else:
        up = getV(n)
        down1 = getV(m)
        down2 = getV( n - m)
        return up // (down1 * down2)
num1 = 0
for i in range(1, n + 1):
    num1 += combination(n, i) * i
print(num1)

num = 0
def dfs (i, path):
    num = path
    for j in range(i + 1, n):
        num += dfs(j, path + 1)
    return num
for i in range(n):
    num += dfs(i, 1)
print(num)

###
# # num = 0
# num = []
# def dfs (i, path, num):
#     # num += path
#     num.append(path)
#     for j in range(i + 1, n):
#         dfs(j, path + 1, num)
#     return
# for i in range(n):
#     dfs(i, 1, num)
# print(sum(num))

# res = []
# members = [i + 1 for i in range(n)]
# def dfs(members, i, path, res):
#     res.append(path)
#     for j in range(i + 1, len(members)):
#         dfs(members, j, path + [members[j]], res)
#     return
# for i, member in enumerate(members):
#     dfs(members, i, [member], res)

# num = 0
# for subset in res:
#     num += len(subset)
# print(num % (pow(10, 9) + 7))