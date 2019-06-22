'''
189. Rotate Array
Easy

1188

583

Favorite

Share
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51462800
The basic idea: reverse 3 times within the array.
a key: k %= nums.length; is very important.
Because k can be larger than length. If this situation occurs, we should take some actions.
Not just return a failure or something.
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)

    def reverse(self, nums, start, end):
        while (end > start):
            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp
            end -= 1
            start += 1

s = Solution()
a = [-1, 2]
s.rotate(a, 2)
print(a)