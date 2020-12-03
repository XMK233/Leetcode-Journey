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