import collections
class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        m = collections.defaultdict(list)
        for road in roads:
            # print(road)
            m[road[0]].append(road[1])
            m[road[1]].append(road[0])
        maxZhi = -1
        for i in range(0, n):
            for j in range(i + 1, n):
                zhi = 0
                len_i = len(m[i])

                len_j = len(m[j])
                if i in m[j]:
                    len_j -= 1
                zhi = len_i + len_j
                if zhi > maxZhi:
                    maxZhi = zhi
        return maxZhi



s = Solution()
print(s.maximalNetworkRank(
    5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
))