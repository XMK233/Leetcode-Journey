'''
[剑指 Offer 51. 数组中的逆序对 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof)

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5

 

限制：

0 <= 数组长度 <= 50000
'''

'''
# https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/zi-wo-gan-jue-dai-ma-bi-guan-fang-jian-ji-shun-bia/
## 这个作者的思路更容易理解.
## 本py文件中的代码实际上是下面那个解析, 代码很难懂. 可以拿来装逼, 但是是在不利于理解和复习.

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/bao-li-jie-fa-fen-zhi-si-xiang-shu-zhuang-shu-zu-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 解析很棒，我自己用归并排序的思路捋了一遍，发现还真是那么回事。
## 解析的图里面，前一段有序经过递归能够返回前一段里面的逆序的对数，同理有一段的逆序对数也由递归得到。
## 问题是，当把这两段合并的时候，怎么统计逆序的对数？
## 其实道理很简单。如果第二段的头一个数字要被拿出来了，说明第二段的头一个数字小于第一段的头一个数字，那么意味着第一段所有的数字都大于第二段的头一个数字，
## 那就可以统计一波逆序对了。
## 然后，接着归并排序，每一次如果第二段的头一个数字小于第一段头一个数字，就差一个统计的过程。最后，你就得到了两端合并的时候的逆序对数。
# 最后，将三部分的逆序对数加起来，就是总数，可以返回了。
# 代码没看，但是思路还算是清晰的，应该就是这样没错了。
'''

class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0

        # 用于归并的辅助数组
        temp = [0 for _ in range(size)]
        return self.count_reverse_pairs(nums, 0, size - 1, temp)

    def count_reverse_pairs(self, nums, left, right, temp):
        # 在数组 nums 的区间 [left, right] 统计逆序对
        if left == right:
            return 0
        mid = (left + right) >> 1
        left_pairs = self.count_reverse_pairs(nums, left, mid, temp)
        right_pairs = self.count_reverse_pairs(nums, mid + 1, right, temp)

        reverse_pairs = left_pairs + right_pairs
        # 代码走到这里的时候，[left, mid] 和 [mid + 1, right] 已经完成了排序并且计算好逆序对

        if nums[mid] <= nums[mid + 1]:
            # 此时不用计算横跨两个区间的逆序对，直接返回 reverse_pairs
            return reverse_pairs

        reverse_cross_pairs = self.merge_and_count(nums, left, mid, right, temp)
        return reverse_pairs + reverse_cross_pairs

    def merge_and_count(self, nums, left, mid, right, temp):
        """
        [left, mid] 有序，[mid + 1, right] 有序

        前：[2, 3, 5, 8]，后：[4, 6, 7, 12]
        只在后面数组元素出列的时候，数一数前面这个数组还剩下多少个数字，
        由于"前"数组和"后"数组都有序，
        此时"前"数组剩下的元素个数 mid - i + 1 就是与"后"数组元素出列的这个元素构成的逆序对个数

        """
        for i in range(left, right + 1):
            temp[i] = nums[i]

        i = left
        j = mid + 1
        res = 0
        for k in range(left, right + 1):
            if i > mid:
                nums[k] = temp[j]
                j += 1
            elif j > right:
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                # 此时前数组元素出列，不统计逆序对
                nums[k] = temp[i]
                i += 1
            else:
                # assert temp[i] > temp[j]
                # 此时后数组元素出列，统计逆序对，快就快在这里，一次可以统计出一个区间的个数的逆序对
                nums[k] = temp[j]
                j += 1
                # 例：[7, 8, 9][4, 6, 9]，4 与 7 以及 7 后面所有的数都构成逆序对
                res += (mid - i + 1)
        return res

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()