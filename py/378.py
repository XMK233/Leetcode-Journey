## https://www.hrwhisper.me/leetcode-kth-smallest-element-sorted-matrix/
## 二分查找.
## 掰开揉碎后, 思路还是蛮简单的. 就是顶一个临时目标值, 如果小于临时目标值的数字不足k个, 那么这个临时目标值就变大, 然后再找.
## 而且, 只要涉及遍历查找的, 都用二分查找来弄.

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix) ## 行数
        L, R = matrix[0][0], matrix[n - 1][n - 1] ## L, R是最大, 最小的数字.
        while L < R:
            mid = L + ((R - L) >> 1) ## mid是介于L, R中间的数字.
            temp = sum([self.binary_search(y,mid,n) for y in matrix]) ## 遍历每一行, 看每一行里面多少个数小于mid, 然后加总, 就知道整个矩阵里面多少个数字小于mid.
            if temp < k:  L = mid + 1 ## 如果temp太小, 就要增大下限, 然后再找一个合适的temp.
            else:  R = mid ## 反之则...
        return L

    def binary_search(self, row, x, n): ## 实际上, 这个函数返回的是, 一行里面有多少个数小于x.
        ## row是矩阵的一行. x是原来的mid. n是行数, 其实也是列数.
        L, R = 0, n
        while L < R:
            mid = (L + R) >> 1
            if row[mid] <= x: L = mid + 1
            else:  R = mid
        return L