# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/31c1aed01b394f0b8b7734de0324e00f?tpId=117&&tqId=37802&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

jindian 17.21
'''
class Solution:
    def maxWater(self , arr ):
        height = arr
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