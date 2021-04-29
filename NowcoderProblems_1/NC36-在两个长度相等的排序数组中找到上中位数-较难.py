# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/6fbe70f3a51d44fa9395cfc49694404f?tpId=117&&tqId=37808&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定两个有序数组arr1和arr2，已知两个数组的长度都为N，求两个数组中所有数的上中位数。
上中位数：假设递增序列长度为n，若n为奇数，则上中位数为第n/2+1个数；否则为第n/2个数
[要求]
时间复杂度为O(logN)O(logN)，额外空间复杂度为O(1)O(1)
示例1
输入
复制
[1,2,3,4],[3,4,5,6]
返回值
复制
3
说明
总共有8个数，上中位数是第4小的数，所以返回3。
示例2
输入
复制
[0,1,2],[3,4,5]
返回值
复制
2
说明
总共有6个数，那么上中位数是第3小的数，所以返回2
备注:
1 \leq N \leq 10^51≤N≤10
5

0 \leq arr_{1i}, arr_{2i} \leq 10^90≤arr
1i
​
 ,arr
2i
​
 ≤10
9

两个方法都可以用. 都要研究研究.
参考的是一个b站的解析: https://www.bilibili.com/video/BV1BA411N7oe/
参考的解法, 其实跟我抄的findMedianinTwoSortedAray1是一样的.
这里有一个细节, 就是length如果是奇偶数, 那么上下边界的移动是不一样的.
直接看并记住findMedianinTwoSortedAray1的解法就行了.
至于为什么要这样求解? 看代码里的注释吧.
'''

class Solution:
    def findMedianinTwoSortedAray1(self, arr1, arr2):
        if not arr1 or not arr2:
            return -1
        n = len(arr1)
        l1, r1, l2, r2 = 0, n - 1, 0, n - 1
        while l1 < r1:
            m1 = (l1 + r1) // 2
            m2 = (l2 + r2) // 2
            length = r1 - l1 + 1
            if arr1[m1] < arr2[m2]: ## 我们以这种情况为例来解释.
                ## 原来的m1左边的一定是比arr1[m1]小, 原来的m2右边的也比arr2[m2]大.
                ## 然后arr1[m1] < arr2[m2]
                ## 所以啊, arr1[m1]右边的以及arr2[m2]左边的这几个数字在一个居中的区间, 这个区间里的数字的大小顺序不明确, 但是中位数一定在其中.
                ## 于是, 调整l1, r2, 好进入这个不明区间, 去进一步缩小中位数的搜索范围.
                l1 = m1 + (1 if length % 2 == 0 else 0)
                r2 = m2
            elif arr1[m1] > arr2[m2]:
                l2 = m2 + (1 if length % 2 == 0 else 0)
                r1 = m1
            else:
                return arr1[m1]
        return (min(arr1[l1], arr2[l2]))

    def findMedianinTwoSortedAray(self, arr1, arr2):
        m = len(arr1)
        return self.helper(arr1, 0, m - 1, arr2, 0, m - 1, m)
    def helper(self, a1, l1, r1, a2, l2, r2, k):
        m = r1 - l1 + 1
        n = r2 - l2 + 1
        if m == 0:
            return a2[l2 + k - 1]
        if k == 1:
            return min(a1[l1], a2[l2])
        i1 = l1 + min(m, k // 2) - 1
        i2 = l2 + min(n, k // 2) - 1
        if a1[i1] > a2[i2]:
            return self.helper(a1, l1, r1, a2, i2 + 1, r2, k - (i2 - l2) - 1)
        else:
            return self.helper(a1, i1 + 1, r1, a2, l2, r2, k - (i1 - l1) - 1)
