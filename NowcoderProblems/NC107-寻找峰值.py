'''
题目描述
山峰元素是指其值大于或等于左右相邻值的元素。给定一个输入数组nums，任意两个相邻元素值不相等，数组可能包含多个山峰。找到索引最大的那个山峰元素并返回其索引。

假设 nums[-1] = nums[n] = -∞。

示例1
输入
复制
[2,4,1,2,7,8,4]
返回值
复制
5

参考了别人的解法. 这道题最核心的地方在于, 寻找的不是最高的山峰, 而是索引值最大的山峰, 也就是最右边的山峰.

'''

#
# 寻找最后的山峰
# @param a int整型一维数组
# @return int整型
#
class Solution:
    def solve(self , a ):
        # write code here
        if a[-2] < a[-1]: return len(a)-1
        for i in range(len(a)-2, -1, -1):
            if a[i-1] <= a[i] and a[i] >= a[i+1]:
                return i