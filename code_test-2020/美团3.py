n = int(input())
A = [int(_) for _ in input().split()]
#####################3
# n = 2
# A = [3, 2]
##########################
B = []
for _1, _2 in enumerate(A):
    ## a已经得到
    a = _2
    i = _1 + 1
    ## i业已得到
    for j in range(1, n+1):
        a = a ^ (i % j)
    B.append(a)

res = B[0]
for i, b in enumerate(B):
    if i == 0:
        continue
    res ^= b

print(res)
