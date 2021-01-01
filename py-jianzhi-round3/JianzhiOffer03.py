'''
[剑指 Offer 03. 数组中重复的数字 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof)

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 


 

限制：

2 <= n <= 100000
'''

'''
因为数字的范围是0~n-1, 也就是说, 理论上每一个数字都应该放在自己的位置上, 比如数字0会位于位置0, 数字1会位于位置1.
所以, 我们将每一个数字都尝试去放到它应该放在的位置.
如果你发现, 诶, 应该放在的位置上已经放了一个适合的数字了, 比如看到一个数字1, 尝试放到位置1上去, 结果发现那里已经有一个1了.
如果这种情况发生, ok直接把这个数字返回即可.

当然, 完全可以考虑使用什么hash表之类的, 用空间换时间.
'''

## 参考: https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/yuan-di-zhi-huan-shi-jian-kong-jian-100-by-derrick/

class Solution:
    def findRepeatNumber(self, nums) -> int:
        for i in range(len(nums)):
            ## 所以, 位置i上放的数字应当是i
            ## 如果nums[i]不是i的话, 就要不断地重复, 直到将合适的数字放到这里为止.
            while nums[i] != i:
                ## 试图把nums[i]放到它该去的地方
                ### 如果它该去的地方已经有一个该放的数字了, 就直接找到重复的了.
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                ### 该去的地方放着的数字不当位
                else:
                    tmp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i] = tmp

        return -1

s = Solution()
print(s.findRepeatNumber([2, 1, 0, 3]))