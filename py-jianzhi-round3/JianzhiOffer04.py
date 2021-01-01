'''
[剑指 Offer 04. 二维数组中的查找 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof)

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

 

注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
'''

'''
参考 https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/

怎么做? 从左下角到右上角, 或者从右上角到左下角.
为什么要从这两个方向出发? 因为这样一来, 你只要大了, 就能朝着一个方向去减小, 小了就反向.
如果不是从这两个方向出发的话, 如果当前数字大了, 你从两个方向走都不太方便, 不知道那条路是正道.
'''
class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        ## 这个i,j就说明了, 我们从左下角开始的.
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False

s = Solution()
print(s.findNumberIn2DArray(
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 20
))
