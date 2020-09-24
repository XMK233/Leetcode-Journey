res = []
def judgement(A):
    for a in A:
        if not(a - 1 == 0 or a - 1 >= 2):
            return "NO"
    return "YES" ## or "YES"
###################################
# import sys
# for i, line in enumerate(sys.stdin):
#     if i % 2 == 0:
#         continue
#     A = [int(_) for _ in line.split()]
#     res.append(judgement(A))
#####################################3
As = [
    [1, 1, 3],
    [1, 2]
]
for A in As:
    res.append(judgement(A))
##########################################3
for r in res:
    print(r)
