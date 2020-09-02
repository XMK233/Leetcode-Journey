class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))

### https://blog.csdn.net/fuxuemingzhu/article/details/79534213
## 思路很清晰.
## 其实不管怎么移动, 都会有这样一个情况:
### 如果旋转了, 那么左半边肯定会比右半边大的.
## 解析里面, 作者提到了一点. 如果mid比right小, 说明mid右边是递增的; 如果mid大于right, 说明mid左边是递增的.
## 把mid的左右两边划分出来了, 就看左右两边的范围是不是能够包括目标值; 哪边包括目标值, 就把下一个区间划到那里.