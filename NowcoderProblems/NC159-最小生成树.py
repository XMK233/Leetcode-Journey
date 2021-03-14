'''
题目描述
一个有n户人家的村庄，有m条路连接着。村里现在要修路，每条路都有一个代价，现在请你帮忙计算下，最少需要花费多少的代价，就能让这n户人家连接起来。
示例1
输入
复制
3,3,[[1,3,3],[1,2,1],[2,3,1]]
返回值
复制
2


'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回最小的花费代价使得这n户人家连接起来
# @param n int n户人家的村庄
# @param m int m条路
# @param cost int二维数组 一维3个参数，表示连接1个村庄到另外1个村庄的花费的代价
# @return int
#
class Solution:
    def miniSpanningTree(self , n , m , cost ):
        # write code here
        return self.way2(n, m, cost)
    def way1(self, n, m, cost): ## Prim算法，不太熟。
        florid = [[float('inf') for j in range(n + 1)] for i in range(n + 1)]
        for i, j, w in cost:
            florid[i][j] = w
        florid[1][1] = 0
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    florid[i][j] = min(florid[i][j], florid[i][k] + florid[k][j])
        ans = 0
        for i in range(1, n+1):
            if florid[1][i] == float('inf'):
                return -1
            else:
                ans = max(ans, florid[1][i])
        return ans
    def way2(self, n, m, cost): ## Kruskal算法，比较简单的最小生成树算法。实现方式是牛客网上的一位前人的实现。
        ## 算法流程：
        ### 按照边的权重排序。
        ### 先从权重小的边开始，把边join起来。
        ### 当然前提是加入新边后不能有环。怎么判断有环与否？当前边的两点若有共同的祖先节点，那就算是有环了。
        ### 直到已加入边的数量达到上限，也就是（节点数-1），就可以终止算法了。
        ## 不过看这位的实现，确实很妙。之前我看的那个实现啊，其实比较麻烦的，所用的数据结构算法啥的也不算多快好省。
        ## 这位的，用一个list：boss就存储了元祖关系，可谓是灰常省事儿了。
        boss = [i for i in range(n + 1)]
        def join(a, b): ## 本质上是构建并查集的。在本题中，用作连接两个点，并判断是否有环。
            def find(x):  ## 寻找x的祖先节点。
                ## 我一开始担心，这个函数跑个不停怎么办。后来发现多虑了，因为终归这个循环是会停的，不会永远循环下去。
                while x != boss[x]:
                    x = boss[x]
                return x
            bossA, bossB = find(a), find(b)
            if bossA == bossB: ## 不能join这一条边。因为构成了环。
                return False
            if bossA > bossB: ## 这里的两个判断，算是对find（）函数功能的一个补充吧。
                boss[bossA] = bossB
            else:
                boss[bossB] = bossA
            return True
        ans = 0
        cost = sorted(cost, key = lambda x: x[2])
        for i, j, w in cost:
            if join(i, j):
                ans += w
        if not ans:
            return -1
        return ans

print(
    Solution().way2(
        9,3,
        [
            [0,1,4],
            [1,2,8],
            [2,3,7],
            [3,4,9],
            [4,5,10],
            [5,6,2],
            [6,7,1],
            [0,7,8],
            [1,7,11],
            [7,8,7],
            [2,8,2],
            [6,8,6],
            [2,5,4],
            [3,5,14],
        ]
    )
)