'''
[剑指 Offer 57. 和为s的两个数字 - 力扣（LeetCode）](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof)

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]


示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]


 

限制：


	1 <= nums.length <= 10^5
	1 <= nums[i] <= 10^6

'''
class Solution:
    def twoSum(self, nums, target):
        array = nums
        tsum = target
        # write code here
        if not array or tsum==0:
            return []
        start = 0
        end = len(array)-1
        while end>start:
            curSum = array[start]+array[end]
            if curSum == tsum:
                return array[start], array[end]
            elif curSum>tsum:
                end-=1
            else:
                start+=1
        return []

## https://blog.csdn.net/mabozi08/article/details/88957275
## 很好玩: "首先选择数组中的第一个数字和最后一个数字，如果它们的和小于s，第一个索引就往右一格，如果它们的和大于s，第二个索引就往左一格。时间复杂度为O(n）"
## 很简单吧? 但是你想得到嘛?


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