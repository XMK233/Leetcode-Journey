'''
[剑指 Offer 41. 数据流中的中位数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof)

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：


	void addNum(int num) - 从数据流中添加一个整数到数据结构中。
	double findMedian() - 返回目前所有元素的中位数。


示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]


示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]

 

限制：


	最多会对 addNum、findMedian 进行 50000 次调用。


注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/
'''

'''
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

这里为什么要用堆呢？因为堆的更新耗时更短。调整一次堆并不一定能够得到一个严格排序的结果，它只能保证堆顶的元素
是最值。不过这也就够了，没必要排序。毕竟我们只想得到中位数。
所以要用堆。
'''

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


##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()