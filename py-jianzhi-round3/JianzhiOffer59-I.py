'''
[剑指 Offer 59 - I. 滑动窗口的最大值 - 力扣（LeetCode）](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof)

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
'''
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

'''
关键操作是, 遍历到某一个点后, 把原有栈里面比这个点小的数全都顶出去. 
'''

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