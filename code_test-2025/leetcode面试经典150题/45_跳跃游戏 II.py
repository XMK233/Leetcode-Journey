'''给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：

0 <= j <= nums[i] 且
i + j < n
返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
 

提示:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
题目保证可以到达 n - 1'''

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        计算到达数组最后一个位置的最小跳跃次数
        
        :param nums: 每个元素表示从该位置向后跳转的最大长度
        :return: 到达最后位置的最小跳跃次数
        """
        # 处理边界情况
        if len(nums) <= 1:
            return 0
        
        # 初始化变量
        jumps = 0  # 跳跃次数
        current_max = 0  # 当前能到达的最远位置
        next_max = 0  # 下一步能到达的最远位置
        
        # 遍历数组（不包括最后一个元素，因为到达最后一个元素后不需要再跳）
        for i in range(len(nums) - 1):
            # 更新下一步能到达的最远位置
            next_max = max(next_max, i + nums[i])
            
            # 当到达当前能到达的边界时，必须进行一次跳跃
            if i == current_max:
                jumps += 1  # 增加跳跃次数
                current_max = next_max  # 更新当前能到达的最远位置
                
                # 如果已经可以到达或超过最后一个位置，可以提前结束
                if current_max >= len(nums) - 1:
                    break
        
        return jumps

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    nums1 = [2, 3, 1, 1, 4]
    solution = Solution()
    result1 = solution.jump(nums1)
    print(f"测试用例1结果: {result1}")  # 预期输出: 2
    
    # 测试用例2
    nums2 = [2, 3, 0, 1, 4]
    result2 = solution.jump(nums2)
    print(f"测试用例2结果: {result2}")  # 预期输出: 2
        