import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        return heapq.nsmallest(k, arr)

# 作者：06ykmqqtt
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/shi-yong-heapqqiu-jie-by-06ykmqqtt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 道理很明显了, 就是用堆排序即可.
## 堆排序有一个特点, 就是第k次堆排序, 就能得到第k小的数字. 比如第一次排序, 就知道最小的数字是多少了.
## 那弄k次, 不就把前k个数字都弄来了嘛.
## 而且python有内置的实现, 岂不美哉?