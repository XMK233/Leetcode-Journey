'''中等
相关标签
premium lock icon
相关企业
提示
给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，
其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，
并且 intervals 按照 starti 升序排列。
同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。

在 intervals 中插入区间 newInterval，
使得 intervals 依然按照 starti 升序排列，
且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 intervals。

注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
 

提示：

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals 根据 starti 按 升序 排列
newInterval.length == 2
0 <= start <= end <= 105'''

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 思路：利用原 intervals 已按起点升序、且不重叠的性质
        # 按顺序遍历，把新区间插入并与有重叠的部分合并
        res: List[List[int]] = []
        i = 0
        n = len(intervals)
        new_start, new_end = newInterval

        # 1. 先把所有在 newInterval 之前、且完全不重叠的区间加入结果
        # 条件：当前区间的结束 < newInterval 的开始
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1

        # 2. 接着处理所有与 newInterval 有重叠的区间
        # 重叠条件：当前区间的开始 <= newInterval 的结束
        # 将这些区间与 newInterval 合并成一个更大的区间
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        # 合并完成后，把合并好的新区间加入结果
        res.append([new_start, new_end])

        # 3. 最后把剩余的、在 newInterval 之后的区间全部加入结果
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1, 3], [6, 9]], [2, 5]))  # [[1,5],[6,9]]
    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1,2],[3,10],[12,16]]
