'''
A国和B国正在打仗，他们的目的是n块土地。现在，A国和B国暂时休战，为了能合理分配这一些土地，AB国开始协商。

A国希望得到这n块土地中的p块土地，B国希望得到这n块土地中的q块土地。每个国家都将自己希望得到的土地编号告诉了小团和小美——两位战争调和人。

你需要帮小团和小美计算，有多少块土地是只有A国想要的，有多少块土地是只有B国想要的，有多少块土地是两个国家都想要的。
'''

n, p, q = [_ for _ in input().split()]
A = [_ for _ in input().split()]
B = [_ for _ in input().split()]

## 每一块土地都是key, 然后国家是value.
## 然后统计多少个key是只有一个value的.
import collections
landToCountry = collections.defaultdict(list)
for a in A:
    landToCountry[a].append("A")
for b in B:
    landToCountry[b].append("B")

aLand = 0
bLand = 0
zhengyi = 0
for land, country in landToCountry.items():
    if len(country) == 2:
        zhengyi+=1
    else:
        if country[0] == "A":
            aLand += 1
        else:
            bLand += 1

print(aLand, bLand, zhengyi)
