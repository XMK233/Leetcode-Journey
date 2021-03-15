# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/09fbfb16140b40499951f55113f2166c?tpId=117&&tqId=37734&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

求平方根.

思路较为简单, 也就是二分查找嘛.
'''


#
#
# @param x int整型
# @return int整型
#
class Solution:
    def sqrt(self, x):
        # write code here
        start = 0
        end = x

        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid
        return end