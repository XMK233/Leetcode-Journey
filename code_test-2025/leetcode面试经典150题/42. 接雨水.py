'''困难
相关标签
premium lock icon
相关企业
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # n 个柱子，两端柱子无法积水
        n = len(height)
        if n <= 2:
            return 0
        # left / right 为当前考察的左右指针
        # left_max / right_max 为从两侧走过来时遇到的最高柱子高度
        # 对于任意位置 i，它能装的水 = min(左侧最高, 右侧最高) - height[i]
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            # 谁更矮，谁就成为当前的“瓶颈侧”
            # 如果左侧柱子更矮，则右侧一定至少有 height[right] 这么高，
            # 此时 min(左侧最高, 右侧最高) 由左侧决定，因此可以安全计算左边位置的水量
            if height[left] < height[right]:
                if height[left] >= left_max:
                    # 更新左侧最高柱子
                    left_max = height[left]
                else:
                    # 左侧最高柱子比当前高，能装的水是二者差值
                    water += left_max - height[left]
                # 这一格的水量已确定，左指针右移
                left += 1
            else:
                # 同理，当右侧更矮时，右侧成为瓶颈侧，
                # 此时 min(左侧最高, 右侧最高) 由右侧决定，可以计算右边位置的水量
                if height[right] >= right_max:
                    # 更新右侧最高柱子
                    right_max = height[right]
                else:
                    # 右侧最高柱子比当前高，能装的水是二者差值
                    water += right_max - height[right]
                # 这一格的水量已确定，右指针左移
                right -= 1
        return water


if __name__ == "__main__":
    sol = Solution()
    cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [1, 0, 2],
        [3, 0, 0, 2, 0, 4],
    ]
    for arr in cases:
        print(f"height = {arr}, trapped water = {sol.trap(arr)}")
