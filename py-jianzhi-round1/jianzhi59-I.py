class Solution:
    def maxSlidingWindow(self, nums, k):
        ## n是窗口的长度
        ## s是数组
        queue = []
        res = []
        ## 滑动窗口的左边沿
        # left = 0
        for idx in range(len(nums)):
            # idx - left 应该小于k.
            if len(queue) > 0 and idx - queue[0] >= k:
                queue.pop(0)
            # queue为空; queue最后面一个元素比目前的num要大
            if len(queue) == 0 or nums[queue[-1]] > nums[idx]:
                queue.append(idx)
            else:
                l = len(queue)
                last_idx_ = l
                for _ in range(l):
                    idx_ = l - 1 - _
                    if nums[queue[idx_]] <= nums[idx]:
                        last_idx_ = idx_
                queue = queue[0:last_idx_]
                queue.append(idx)
            if idx >= k - 1:
                res.append(nums[queue[0]])
        return res

# s = Solution()
# print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
## https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/dan-diao-dui-lie-xiang-jie-by-carlsun-2/
## https://leetcode-cn.com/problems/sliding-window-maximum/solution/shuang-duan-dui-lie-jie-jue-hua-dong-chuang-kou--2/
## 原理参考了上述两个链接，然后实现是自己弄的。因为链接里面提供的解都不是python。