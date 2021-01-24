'''
[剑指 Offer 53 - I. 在排序数组中查找数字 I - 力扣（LeetCode）](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof)

统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

 

限制：

0 <= 数组长度 <= 50000

 

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        ## 这里的right相当于第一个大于target的数所在的index
        if left == right:
            return 0
        return right - left

    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))

### https://blog.csdn.net/fuxuemingzhu/article/details/83273084
## 这道题就是判断目标值的higher和lower边界何在.
## 你发现这两个方法有什么区别了没有. 一个是小于号, 另一个是小等于.
## 这两个方法, 建议直接背住就好了. 以后可能用得上. 这是个技巧.

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