# from itertools import combinations
m = int(input())
n = int(input())
# m = 6
# n = 2
rst = 1
for j in range(n):
    part1 = m - j
    part2 = j + 1
    rst = rst * float(part1) // part2
    # rst *= (m - j) // (j + 1)
print(rst)