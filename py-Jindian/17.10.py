'''
[面试题 17.10. 主要元素 - 力扣（LeetCode）](https://leetcode-cn.com/problems/find-majority-element-lcci)

数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5

 

示例 2：

输入：[3,2]
输出：-1

 

示例 3：

输入：[2,2,1,1,1,2,2]
输出：2

 

说明：
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？
'''

'''
这个方法我懂得, 但是关键是只懂了一半. 
参考了https://leetcode-cn.com/problems/find-majority-element-lcci/solution/mo-er-tou-piao-fa-by-yi-wen-statistics/ 
进行改正, 并发现, 这种方法叫摩尔投票法. 
'''

class Solution:
    def majorityElement(self, nums):
        if len(nums) == 0:
            return -1
        #####
        curNum = None
        curCnt = 0
        for num in nums:
            if curCnt == 0:
                curNum = num
                curCnt += 1
            else:
                if curNum != num:
                    curCnt -= 1
                    if curCnt == 0:
                        ## 第一次提交的时候
                        curNum = None
                else:
                    curCnt += 1
        if curCnt == 0:
            return -1
        ## 第二次修改, 增加了以下的判断.
        ## 你其实可以知道, 上面的流程走过后, curNum未必是出现次数最多的.
        ## 所以再增加一个遍历的阶段, 如果curNum统计的出现次数确实过半, 才说明这个数是主要元素.
        count = 0
        for num in nums:
            if num == curNum: count += 1
            if count > len(nums)/2:
                return curNum
        return -1

print(
    Solution().majorityElement([1, 2, 3])
)