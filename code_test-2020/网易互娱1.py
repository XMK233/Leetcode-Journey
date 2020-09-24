## AC了. 这个题是问你, 哦, 一个SQL语句, 用编程语言重新实现.

n = int(input())

import collections
idToName = {}
nameToId = collections.defaultdict(list)
for i in range(n):
    id, name = input().split()
    idToName[id] = name
    nameToId[name].append(id)

count = 0
for name in nameToId.keys():
    if len(nameToId[name]) >= 2:
        count += 1

print(count)