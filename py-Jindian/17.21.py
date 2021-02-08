'''
[面试题 17.21. 直方图的水量 - 力扣（LeetCode）](https://leetcode-cn.com/problems/volume-of-histogram-lcci)

给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        # 两个以下的宽度无法蓄水
        if len(height) <= 2:
            return 0
        height_max = max(height)  # 最高柱高度
        water = [height_max] * len(height)  # 假设水都能装到最高柱，当然可能性不大

        def updata_height(start, end, step):
            hand = 0  # 指针之前的高度
            for i in range(start, end, step):
                hand = max(height[i], hand)
                if hand == height_max:
                    break
                water[i] = hand

        updata_height(0, len(height), 1)  # 从前往后
        updata_height(len(height) - 1, -1, -1)  # 从后往前

        # 蓄水高度 - 石头高度
        return sum(water) - sum(height)


# 作者：ProgrammerPlus
# 链接：https: // leetcode - cn.com / problems / volume - of - histogram - lcci / solution / dai - ma - hao - li - jie - you - xie - rong - yu - deng - wo - xin - qing /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。