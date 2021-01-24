'''
[剑指 Offer 13. 机器人的运动范围 - 力扣（LeetCode）](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof)

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3


示例 2：

输入：m = 3, n = 1, k = 0
输出：1


提示：


	1 <= n,m <= 100
	0 <= k <= 20

'''
'''
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 实际上是一个典型的dfs流程。也就是判断一下，是否有越界，是否满足限定条件k，就行了，没什么花架子。
## si，sj就是i和j的位数和。其中计算si和sj是有技巧的，也就是说，比如i，j分别增加了1，减少了1，用不着全部重新算一遍，只需要微量调整一下就可以了。你自己整两个例子，看看是不是这么回事。
这道题有点好玩的地方. 就是作者只有向右和向上的操作. 没有其他方向的操作. 
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)



##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()