#python。但是好像除了用了一下len（）求数组长度，就没有用python的内置函数了。感觉用其他语言也能实现。#

#关键点：网上有很多题解，主要参考的是这篇 http://blog.csdn.net/u010235142/article/details/50134393 ，这里说一下我的感受。
#因为时间复杂度是log，那么就不能遍历了，只能用二分来查找。
#其实，这里不需要我们做归并排序，只需要找出第k个数就行了。
#进入递归的时候，k就是总数的一半。
#每个数组各自拿自己第k/2位置的数字对比，假设a[k/2] > b[k/2]，就说明a和b归并后的数组的前k个数字里面，b的k/2位置之前的数字肯定都在其中。
#然后到b的后面一些的位置去找。
#注意数组长度的问题，比如a或者b的总长度都已经小于k/2了；或者我们要找的数字恰好就是归并后的第一个数字，那岂不就正好是a和b两个数组里面第一个数字更小的那个吗？#

#细节：python的数组比较不方便，不像C++可以通过数组名加多少来实现数组头的向后移动。
#Python3的/除法，得到的结果自动作为float，有的地方需要整除，就要用//，有的地方需要浮点数的除法，就得用/，这里要小心。

class Solution:
    def findKth(self, nums1, head1, m, nums2, head2, n, k):
        if m > n:
            return self.findKth(nums2, head2, n, nums1, head1, m, k)
        # m <= n is guaranteed
        if m == 0:
            return nums2[head2 + k - 2]
        if k == 1:
            return min(nums1[head1 - 1], nums2[head2 - 1])

        p1 = min(k // 2, m)
        p2 = k - p1

        if nums1[head1 + p1 - 2] < nums2[head2 + p2 - 2]:
            return self.findKth(nums1, head1 + p1, m - p1, nums2, head2, n, k - p1)
        elif nums1[head1 + p1 - 2] > nums2[head2 + p2 - 2]:
            return self.findKth(nums1, head1, m, nums2, head2 + p2, n - p2, k - p2)
        else:
            return nums2[head2 + p2 - 2]

    def sub(self, nums1, m, nums2, n):
        total = m + n
        head1 = 1
        head2 = 1
        if total % 2 == 1:
            return self.findKth(nums1, head1, m, nums2, head2, n, (total + 1) // 2)
        else:
            return (self.findKth(nums1, head1, m, nums2, head2, n, total // 2) + self.findKth(nums1, head1, m, nums2, head2, n,
                                                                                   total // 2 + 1)) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        #print(self.sub(nums1, m, nums2, n))
        return self.sub(nums1, m, nums2, n)