import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 初始化大顶堆和小顶堆
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):# 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:  # 先加到小顶堆，再把小堆顶元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]

# 作者：z1m
# 链接：https://leetcode-cn.com/problems/find-median-from-data-stream/solution/tu-jie-pai-xu-er-fen-cha-zhao-you-xian-dui-lie-by-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 其实最基本的算法就是, 将原来的完整数组给他拆分成两个部分, 大的一半, 小的一半.
## 然后大的那一半是小顶堆, 也就是说, 堆顶元素是大的那一半里面的最小值, 就是凤尾.
## 小的那一半是大顶堆, 堆顶是小的一半里面最大的那个值, 也就是鸡头.
## 如果总共有奇数个数字, 那么"凤"数组要多一个.
## 每一次新增一个数字, 如果此时鸡和凤组数量一样多, 那么先把这个数字给鸡组, 排序后, 再将鸡头加到凤组, 然后排序, 就完事了.
## 如果凤组比鸡组多, 那么就先进凤组, 排序后, 将凤尾送给鸡组再排序即可.
## 为什么要这么安排? 你会发现反过来弄更麻烦.