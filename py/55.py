## https://blog.csdn.net/fuxuemingzhu/article/details/83504437
## 道理很简单啊. 看看代码即可理解. 入口即化.
## 这道题体现出来的就是所谓的贪心. 每次都看最优的情况即可.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True