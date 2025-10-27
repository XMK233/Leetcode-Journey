# 56. 合并区间
# 中等

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并所有重叠的区间，并返回一个不重叠的区间数组
        
        思路解析：
        1. 首先按照每个区间的起始位置进行排序
        2. 创建一个结果列表，将第一个区间添加进去
        3. 遍历剩余的所有区间，对于每个区间：
           - 如果当前区间的起始位置小于等于结果列表中最后一个区间的结束位置，则合并这两个区间
           - 否则，将当前区间添加到结果列表中
        4. 返回结果列表
        
        参数:
            intervals: List[List[int]] - 若干个区间的集合
        
        返回:
            List[List[int]] - 合并后的不重叠区间数组
        """
        # 如果输入为空，直接返回空列表
        if not intervals:
            return []
        
        # 按照区间的起始位置进行排序
        intervals.sort(key=lambda x: x[0])
        
        # 创建结果列表，并将第一个区间添加进去
        merged = [intervals[0]]
        
        # 遍历剩余的区间
        for i in range(1, len(intervals)):
            # 获取结果列表中的最后一个区间
            last = merged[-1]
            # 获取当前要处理的区间
            current = intervals[i]
            
            # 如果当前区间的起始位置小于等于结果列表中最后一个区间的结束位置，说明有重叠
            if current[0] <= last[1]:
                # 合并这两个区间，更新结束位置为较大的那个值
                merged[-1] = [last[0], max(last[1], current[1])]
            else:
                # 没有重叠，直接添加到结果列表中
                merged.append(current)
        
        return merged

# 测试样例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1: 有重叠区间
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    # 预期结果: [[1,6],[8,10],[15,18]]
    # 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"测试用例1: intervals={intervals1}")
    print(f"结果: {solution.merge(intervals1)}")
    
    # 测试用例2: 有重叠区间
    # intervals = [[1,4],[4,5]]
    # 预期结果: [[1,5]]
    # 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
    intervals2 = [[1, 4], [4, 5]]
    print(f"测试用例2: intervals={intervals2}")
    print(f"结果: {solution.merge(intervals2)}")
    
    # 测试用例3: 无重叠区间
    # intervals = [[1,2],[3,4],[5,6]]
    # 预期结果: [[1,2],[3,4],[5,6]]
    intervals3 = [[1, 2], [3, 4], [5, 6]]
    print(f"测试用例3: intervals={intervals3}")
    print(f"结果: {solution.merge(intervals3)}")
    
    # 测试用例4: 复杂重叠情况
    # intervals = [[1,5],[2,3],[4,6],[7,9],[8,10]]
    # 预期结果: [[1,6],[7,10]]
    intervals4 = [[1, 5], [2, 3], [4, 6], [7, 9], [8, 10]]
    print(f"测试用例4: intervals={intervals4}")
    print(f"结果: {solution.merge(intervals4)}")