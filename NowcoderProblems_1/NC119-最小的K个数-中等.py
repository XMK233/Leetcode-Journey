# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=117&&tqId=37765&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。如果K>数组的长度，那么返回一个空的数组
示例1
输入
复制
[4,5,1,6,2,7,3,8],4
返回值
复制
[1,2,3,4]

很简单，直接用堆。

'''
# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        res = []
        for i in range(k):
            heapq.heapify(tinput)

            res.append(tinput.pop(0))
        return res

print(
    Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4)
)