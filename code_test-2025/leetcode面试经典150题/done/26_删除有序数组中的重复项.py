'''给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k。去重后，返回唯一元素的数量 k。

nums 的前 k 个元素应包含 排序后 的唯一数字。下标 k - 1 之后的剩余元素可以忽略。

判题标准:

系统会用下面的代码来测试你的题解:

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有断言都通过，那么您的题解将被 通过。

 

示例 1：

输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4,_,_,_,_,_]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
 

提示：

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums 已按 非递减 顺序排列。'''
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        删除有序数组中的重复项，返回删除后数组的新长度
        
        :param nums: 非严格递增排列的数组
        :return: 删除重复项后的数组长度
        """
        # 处理边界情况
        if not nums:
            return 0
        
        # 双指针方法
        # k 表示当前唯一元素应该放置的位置
        # 初始时，第一个元素一定是唯一的，所以 k = 1
        k = 1
        
        # i 从第二个元素开始遍历数组
        for i in range(1, len(nums)):
            # 如果当前元素与前一个唯一元素不同，则它是一个新的唯一元素
            if nums[i] != nums[k - 1]:
                # 将该元素放到正确的位置
                nums[k] = nums[i]
                # 更新唯一元素的位置指针
                k += 1
        
        # 返回唯一元素的数量
        return k

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    nums1 = [1, 1, 2]
    solution = Solution()
    k1 = solution.removeDuplicates(nums1)
    print(f"测试用例1结果: k = {k1}, nums = {nums1[:k1]}")  # 预期输出: k = 2, nums = [1, 2]
    
    # 测试用例2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(f"测试用例2结果: k = {k2}, nums = {nums2[:k2]}")  # 预期输出: k = 5, nums = [0, 1, 2, 3, 4]
        