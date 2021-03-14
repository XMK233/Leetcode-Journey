# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/e016ad9b7f0b45048c58a9f27ba618bf?tpId=117&&tqId=37791&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
有一个整数数组，请你根据快速排序的思路，找出数组中第K大的数。

给定一个整数数组a,同时给定它的大小n和要找的K(K在1到n之间)，请返回第K大的数，保证答案存在。

示例1
输入
复制
[1,3,5,2,2],5,3
返回值
复制
2

还是老样子，就是直接用heapq来弄。
'''

# -*- coding:utf-8 -*-
import heapq
class Solution:
    def findKth(self, a, n, K):
        # write code here
        # if K > len(n):
        #     return
        nums = [-1 * i for i in a]
        res = []
        for k in range(K):
            heapq.heapify(nums)
            res.append(-1 * nums.pop(0))
        return res[-1]

print(
    Solution().findKth([1,3,5,2,2],5,3)
)
