class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 实际上是一个典型的dfs流程。也就是判断一下，是否有越界，是否满足限定条件k，就行了，没什么花架子。
## si，sj就是i和j的位数和。其中计算si和sj是有技巧的，也就是说，比如i，j增加了1，减少了1，用不着全部重新算一遍，只需要微量调整一下就可以了。你自己整两个例子，看看是不是这么回事。