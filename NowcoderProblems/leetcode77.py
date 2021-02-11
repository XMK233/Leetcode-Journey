'''
https://leetcode-cn.com/problems/combinations/

77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''
import itertools
class Solution:
    def combine(self, n: int, k: int):
        return list(itertools.combinations(range(1, 1+n), k))

print(Solution().combine(4, 2))