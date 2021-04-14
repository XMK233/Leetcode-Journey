# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/7cd13986c79d4d3a8d928d490db5d707?tpId=117&&tqId=37744&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出一个转动过的有序数组，你事先不知道该数组转动了多少
(例如,0 1 2 4 5 6 7可能变为4 5 6 7 0 1 2).
在数组中搜索给出的目标值，如果能在数组中找到，返回它的索引，否则返回-1。
假设数组中不存在重复项。
示例1
输入
复制
[1],0
返回值
复制
-1
示例2
输入
复制
[3,2,1],1
返回值
复制
2

可以参考剑指offer11.
不过这题的思路还是有所不同.
主要的技巧在于, 根据mid的左右两边哪边是有序的, 就单独判断一下.
'''
class Solution:
    def search(self , A , target ):
        # write code here
        n = len(A)
        l = 0
        r = n - 1
        while l<=r:
            mid = (l+r)//2
            if target == A[mid]:
                return mid

            if A[mid] >= A[r]: ## 左边有序
                if  A[l] <= target < A[mid]: ## 如果target值介于有序的部分之间
                    r = mid-1
                else: ## 否则
                    l = mid+1
            else: ## 右边有序
                if A[mid] < target <= A[r]: ## 那么就跟前面的反过来就好了.
                    l = mid+1
                else:
                    r = mid-1
        return -1

print(
    Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
)