## 很简单.
# 首先, 这个题目要输出的东西是什么要搞清楚, 不是数字, 而是数字对应的index.
# 遍历到2的时候, 把2跟目标值的差值, 也就是7, 记录进字典作为key, 对应的value是这个2的index也就是0.
## 这么做的意义是什么呢? 当日后发现远数组里面有7的时候, 就去查字典, 得到0, 就是能够和7组成目标值的那个数字的index.
## 一句话: {某值和目标值的差值: 某值的index}, 然后遍历其他值去字典里查, 得到某值的index, 于是[某值, 其他值] 就是结果了.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        dic = {}
        nums_length = len(nums)
        for n in range(nums_length):
            if nums[n] in dic:
                result.append(dic[nums[n]])
                result.append(n)
                break
                pass
            else:
                dic[target - nums[n]] = n
        return result

s = Solution()
print(s.twoSum([2, 7, 11, 15],9))