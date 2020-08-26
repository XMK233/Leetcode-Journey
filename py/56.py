# https://blog.csdn.net/XX_123_1_RJ/article/details/84320632
## 思路是采用上述方法, 但是由于数据结构变了, 我也就改变了一下数据结构处理方式, 同时也重新设计了
## 算法.
class Solution:
    def merge(self, intervals):
        ## 如果intervals有点问题, 就酱紫处理.
        if len(intervals) <= 1: return intervals
        ## 初始化一个字典.
        zones = {} # collections.defaultdict(list)
        for start, end in intervals:
            if start not in zones:
                zones[start] = end
            else:
                if end > zones[start]:
                    zones[start] = end
            # r = zones.get(start)
            # if r:
            #     if end > r[-1]:
            #         r[-1] = end
            # else:
            #     zones[start].append(end)
        ## 根据开始时间来进行排序. 呵呵哒.
        starts = list(zones.keys())
        starts.sort()
        # for start in starts:
        #     print(start, zones[start])
        ##
        print(starts[0], zones[starts[0]])
        res = [
            [starts[0], zones[starts[0]]]
        ]
        for i, s in enumerate(starts, start= 1):
            e = zones[s]
            if s <= res[-1][-1]:
                res[-1][-1] = max(e, res[-1][-1])
            else:
                res.append([s, e])
        return res


        # intervals.sort(key=lambda x: x.start)  # 按照第一个关键字，从小到大排序
        # res = [intervals[0]]  # 定义结果列表，并把第一个元素放进去
        # for i, e in enumerate(intervals, start=1):  # 依次添加新元素，并考虑重叠问题
        #     if e.start <= res[-1].end:
        #         res[-1].end = max(res[-1].end, e.end)  # 合并
        #     else:
        #         res.append(e)
        # return res

s = Solution()
res = s.merge(
    [[1, 3], [1, 4], [2, 6], [8, 10], [15, 18]]
)
print(res)

