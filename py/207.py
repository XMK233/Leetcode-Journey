## https://blog.csdn.net/XX_123_1_RJ/article/details/84787393
## 关键词: 有向无环图, 无环则OK. 记录访问与否是visit数组, 记录图是graph图.
## 用dfs来判断一个点出发的图是不是无环.
## dfs的时候记得要剪枝, 以减少消耗.

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:  # 转换成邻接表的形式
            graph[x].append(y)

        def dfs(graph, v):  # 从顶点v 出发深度优先搜索图G，判断图中是否存在回路
            visit[v] = -1  # 访问过标记

            for w in graph[v]:  # 遍历 v 的邻接点
                if visit[w] == -1: return False  # 如果w已经访问过，必存在回路，直接返回即可
                if visit[w] == 1: continue  # 剪枝

                if not dfs(graph, w): return False  # 如果从w出发，发现回路，则返回（进入递归调用）

            visit[v] = 1  # 被访问过，从这个点从发得到的结果是正确的，标记1，避免下次继续访问，剪枝情况
            return True

        for v in range(numCourses):
            if not dfs(graph, v):
                return False
        return True