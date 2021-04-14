# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/31c1aed01b394f0b8b7734de0324e00f?tpId=117&&tqId=37802&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器，请返回容器能装多少水。
示例1
输入
复制
[3,1,2,5,2,4]
返回值
复制
5
示例2
输入
复制
[4,5,1,3,2]
返回值
复制
2
备注:
1 \leq N \leq 10^61≤N≤10
6

jindian 17.21 是Solution, 然后参考了一个其他的方法是solution1.
后者更快更省. 应当好好学一学.
'''

class Solution:
    def trap(self, height) -> int:
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

class Solution1:
    def maxWater(self , arr ):
        # write code here
        if arr is None or len(arr)<=2:
            return 0
        low = arr[0] ## low指的是当前的可能最高水位的高度.
        tmp = 0 ## tmp是临时储水量的计量
        ans=0 ## 最终答案.
        maxh=max(arr) ## 最高海拔何在.
        idxh=arr.index(maxh) ##
        for i in arr[:idxh+1]: ## 最高海拔左边的部分
            if i<low: ## 如果遍历到海拔低于low, 说明这个高度是浸没在水下的. 要计算水量哦.
                tmp += low-i
            else: ## 如果当前海拔高于low, 那么海平面就被提高到i的高度, 所以要改变low的值, 然后tmp加到ans里面, 然后tmp要归零重计.
                ans+=tmp
                tmp=0
                low=i
        ## 最高海拔右边的部分, 从数组的后面再倒着重复一遍上面的过程, 以统计后半部分的水量.
        low = arr[-1]
        tmp = 0
        for i in arr[idxh:][::-1]:
            if i<low:
                tmp += low-i
            else:
                ans+=tmp
                tmp=0
                low=i
        return ans
print(
    Solution1().maxWater([3, 1, 2, 5, 2, 4])
)