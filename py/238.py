class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        _len = len(nums)
        prod = 1
        for i in range(_len):
            answer.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(_len - 1, -1, -1):
            answer[i] *= prod
            prod *= nums[i]
        return answer

#  https://blog.csdn.net/fuxuemingzhu/article/details/79325534
## 第一遍, 正着遍nums, 得到某一个数左边所有的数的乘积
## 第二遍, 反着遍历nums，得到某一个数右边所有的数的乘积
## 然后你就懂了。