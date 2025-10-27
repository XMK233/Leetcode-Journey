'''给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

根据维基百科上 h 指数的定义：h 代表"高引用次数" ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。

 

示例 1：

输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
示例 2：

输入：citations = [1,3,1]
输出：1
 

提示：

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000'''
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        计算研究者的h指数
        
        Args:
            citations: 表示研究者每篇论文被引用次数的整数数组
            
        Returns:
            研究者的h指数，即最大的h值，使得至少有h篇论文被引用了至少h次
        """
        # 对引用次数进行降序排序
        citations.sort(reverse=True)
        
        h = 0
        # 遍历排序后的数组，寻找最大的h值
        for i in range(len(citations)):
            # 如果当前论文的引用次数大于等于已计算的h值+1
            # 则h可以增加1
            if citations[i] > h:
                h += 1
            else:
                # 一旦遇到引用次数不满足条件的论文，后续论文引用次数更少
                # 所以可以提前结束遍历
                break
        
        return h


# 测试用例
solution = Solution()

# 测试用例1：[3,0,6,1,5]
# 预期输出：3
result1 = solution.hIndex([3,0,6,1,5])
print(f"测试用例1结果: {result1}")

# 测试用例2：[1,3,1]
# 预期输出：1
result2 = solution.hIndex([1,3,1])
print(f"测试用例2结果: {result2}")

# 测试用例3：[0]
# 预期输出：0
result3 = solution.hIndex([0])
print(f"测试用例3结果: {result3}")

# 测试用例4：[100]
# 预期输出：1
result4 = solution.hIndex([100])
print(f"测试用例4结果: {result4}")
        