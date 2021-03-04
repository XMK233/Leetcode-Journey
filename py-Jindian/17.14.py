'''
[面试题 17.14. 最小K个数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/smallest-k-lcci)

设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]


提示：


	0 <= len(arr) <= 100000
	0 <= k <= min(100000, len(arr))

'''
import heapq

class Solution:
    def smallestK1(self, arr, k):
        res =[]
        if k == 0:
            return res
        heap = [-x for x in arr[:k]]
        heapq.heapify(heap)
        for i in range(k, len(arr)):
            if arr[i] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -arr[i])
        res = [-x for x in heap]
        return res

    def smallestK(self, arr, k):
        res = []
        if k == 0:
            return res
        heap = [x for x in arr]
        for i, j in zip(range(len(arr)), range(k)):
            heapq.heapify(heap)
            res.append(heap.pop(0))
        return res


print(Solution().smallestK([1,3,5,7,2,4,6,8], 4))

# 作者：LionKing865
# 链接：https://leetcode-cn.com/problems/smallest-k-lcci/solution/python3-zui-da-dui-1714-by-lionking865-z4nu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。