class Solution:
    def minmumNumberOfHost(self, n, startEnd):
        start = list()
        end =list()
        #分别得到活动起始时间
        for i in range(n):
            start.append(startEnd[i][0])
            end.append(startEnd[i][1])
        #分别对开始和结束时间排序
        start.sort()
        end.sort()
        res = 0
        j = 0
        for i in range(n):
            #新开始的节目大于上一轮结束的时间，主持人不变
            if start[i] >= end[j]:
                j += 1
            else:
                #主持人增加
                res += 1
        return res


s = Solution()
print(
    s.minmumNumberOfHost(2, [[1,2], [3,4]])
)