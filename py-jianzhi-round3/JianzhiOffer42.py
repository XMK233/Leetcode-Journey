'''
[剑指 Offer 42. 连续子数组的最大和 - 力扣（LeetCode）](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof)

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

 

提示：


	1 <= arr.length <= 10^5
	-100 <= arr[i] <= 100


注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

 
'''

'''
## 答案的思路是：构建dp数组，dp[i]的意义是，以这个nums[i]结尾的数组里面最大的和。
## 当然了，这个解并没有构建一个dp数组，可能是因为作者将其优化了吧。

所以这个题目的思路到底是什么？就是动态规划。
如果prev>=0，那就cur + prev，否则cur + 0. 
然后遍历到最后即可。
'''
# https://blog.csdn.net/fuxuemingzhu/article/details/71101802
## 参考这个人的解析里面的状态转移公式.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        cur, prev = 0, 0
        res = float("-inf")
        for i in range(N):
            cur = nums[i] + (prev if prev > 0 else 0)
            prev = cur
            res = max(res, cur)
        return res

## 答案的思路是：构建dp数组，dp[i]的意义是，以这个nums[i]结尾的数组里面最大的和。
## 当然了，这个解并没有构建一个dp数组，可能是因为作者将其优化了吧。


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