#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
class Solution:
    def helper(self, a, start, end, K):
        low, high = start, end
        key = a[start]
        while start < end:
            while start < end and a[end] <= key:
                end -= 1
            a[start] = a[end]
            while start < end and a[start] >= key:
                start += 1
            a[end] = a[start]
        a[start] = key
        if start < K - 1:
            return self.helper(a, start + 1, high, K)
        elif start > K - 1:
            return self.helper(a, low, start - 1, K)
        else:
            return a[start]
        
    def findKth(self , a, n, K):
        return self.helper(a, 0, n-1, K)

print(
    Solution().findKth(

[10,10,9,9,8,7,5,6,4,3,4,2],12,3
    )
)

