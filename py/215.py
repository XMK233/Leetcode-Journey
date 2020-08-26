## 这道题的技巧是: 用大顶堆来处理. 大顶堆每一次都要弹出堆顶的那个值, 也就是当前最大值, 所以只要我们能够弹出k次就行了.
## https://blog.csdn.net/XX_123_1_RJ/article/details/80819850
## 介绍了python自带的大顶堆怎么用.
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]