'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
 

提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 初始化候选元素和计数器
        candidate = None
        count = 0
        
        # 遍历数组
        for num in nums:
            if count == 0:
                # 如果计数器为0，说明当前元素是新的候选元素
                candidate = num
                count = 1
            elif candidate == num:
                # 如果当前元素与候选元素相同，计数器加1
                count += 1
            else:
                # 如果当前元素与候选元素不同，计数器减1
                count -= 1
        
        # 最后剩下的候选元素就是多数元素
        return candidate