class Solution:
    def constructArr(self, a):
        # 从左到右, 再从右向左遍历
        # 维护前缀积数组, 从右向左遍历时只需要维护后缀积即可, 然后乘以前一个前缀积, 其结果即为当前元素的左右元素乘积
        lefts = []
        left = 1
        for x in a:
            left *= x
            lefts.append(left)
        # 这里只需要维护后缀积, 没必要再建立一个后缀积数组
        right = 1
        res = [0] * len(a)
        for i in range(len(a))[::-1]:
            # 注意下标为0时左侧没有元素, 此时左侧部分乘积置为1
            left = lefts[i - 1] if i > 0 else 1
            res[i] = left * right
            # 注意当前元素处理完之后再乘以它, 因为结果是不包含当前元素自身的
            right *= a[i]
        return res

# s = Solution()
# print(s.constructArr([1,2,3,4,5]))
## https://blog.nowcoder.net/n/38b43ec43cb94fcc8e7bfcfe7f8e69a8
## 怎么理解? 其实道理很简单, 就是tnd把左边的都乘起来, 然后右边的也都乘起来,
## 然后选择一个数两边的累积的积, 就得到了目标了.