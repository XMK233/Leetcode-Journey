## https://blog.csdn.net/fuxuemingzhu/article/details/79826703
## 其实思路很简单. 就是依次找最小和次小的数字, 如果有第三个数字比它俩大, 直接返回true即可.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False