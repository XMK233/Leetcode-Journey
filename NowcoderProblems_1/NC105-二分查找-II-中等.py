'''
https://www.nowcoder.com/practice/4f470d1d3b734f8aaf2afb014185b395?tpId=117&tqId=37829&companyId=665&rp=1&ru=%2Fcompany%2Fhome%2Fcode%2F665&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

题目描述
请实现有重复数字的升序数组的二分查找
给定一个 元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1
示例1
输入
复制
[1,2,4,4,5],4
返回值
复制
2
说明
从左到右，查找到第1个为4的，下标为2，返回2
示例2
输入
复制
[1,2,4,4,5],3
返回值
复制
-1
示例3
输入
复制
[1,1,1,1,1],1
返回值
复制
0

可以采用剑指offer53I的思路.
当然, 参考的另一种实现也就是search1更好理解, 也不容易记错.
'''
import sys
class Solution:
    def search(self, nums, target):
        left = self.lowwer_bound(nums, target)
        return left
    def lowwer_bound(self, nums, target):
        ## 其实这里有一点技巧.
        ## 这个是用来找下界的, 类似的道理可以用来找上界.
        left, right = 0, len(nums) ## "左"边那个, left, 就是最左边的那个位置也就是0; "右"边的那个, right, 是要比规定的nums的最后一个下标多1的哟.
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1 ## left往"右"移的, 也要移到比mid多1的位置哟.
            else:
                right = mid ## 往左移动的, 就不要放到mid少1的位置了, 直接放在mid即可. 好方便呀.
        if nums[left] != target:
            return -1
        else:
            return left

    def search1(self, nums, target):
        # write code here
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # 保证找到的target是第一次出现
                while mid != 0 and nums[mid - 1] == nums[mid]:
                    mid -= 1
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

s = Solution()
print(
    s.search([-2, -1, 0, 1, 2, 3, 4, 5],-3)
)