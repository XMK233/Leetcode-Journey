## https://blog.csdn.net/fuxuemingzhu/article/details/79391342
## 一点技术含量都没有. 我操.
## 每一次要调用shuffle, 就调用random直接shuffle就好了. 其实也暗合了程序员的数学里面说的,
## 不要尝试自己实现随机算法.
## 然后永远保留一个副本, 以便返回初始状态.

import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums_s = self.nums[:]
        random.shuffle(nums_s)
        return nums_s


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()