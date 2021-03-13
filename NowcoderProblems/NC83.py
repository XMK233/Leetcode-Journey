#
#
# @param arr double浮点型一维数组
# @return double浮点型
#
'''
题目描述
给定一个double类型的数组arr，其中的元素可正可负可0，返回子数组累乘的最大乘积。
示例1
输入
复制
[-2.5,4,0,3,0.5,8,-1]
返回值
复制
12.00000

这道题有点类似于子数组和最大值的那道题, 但是由于乘法能够很快地改变符号导致大小之势异也, 这一点远复杂于和的那道原题.
参考了别人的代码实现, 非常好, 值得学习.
实现较为简单, 一看便知.
'''
class Solution:
    def maxProduct(self , arr ):
        if arr == []: return 0.0
        imax ,imin ,res = arr[0], arr[0], arr[0]
        for i in range(1,len(arr)):
            imax = max(arr[i] * imax, arr[i] * imin, arr[i])
            imin = min(arr[i] * imax, arr[i] * imin, arr[i])
            res = max(res,imax)
        return res