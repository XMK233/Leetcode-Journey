## https://www.geek-share.com/detail/2712927775.html
## 直接参考了别人的做法.
## 首先, 我们不能碰到一个0就贸然改变该行该列的值, 否则, 改完后, 你会把后续要遍历的, 不是0的点变成0, 那就会错掉.
## 所以, 需要用某种方法记住, 哪些位置原本是0. 标记完后, 再做一遍遍历, 将该变成0的行列给他变化掉.
## 怎么记住? 用m*n的矩阵可以记, 用m和n的数组分别记住行和列亦可, 但是这些的空间复杂度都不是常数.
## 所以, 可以考虑用矩阵的第一行和第一列来记录. 比如, 碰到(i, j)位置是0, 那就把(0, j), (i, 0)这两个位置直接设置为0. 因为它们终究也是要变为0的, 先变了也没事.
## 然后, 再从下到上, 从右到左遍历, 如果碰上(0, j), (i, 0)这两个位置任意一个是0, 那么就把(i, j)设为0.
## 然后, 如果初始0一开始就在第0列, 那么就意味着这一列就要被全置零. 就用一个变量hasZeros来标记, 是否要将头一列置零. 所以, 头一列置零与否, 由一个专门的变量标记, 这也就满足了空间复杂度为常数的要求.

class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return
        hasZeros = 0
        for i in range(m):  # 第i行
            if matrix[i][0] == 0:  # 第i行的第零列
                hasZeros = 1
            for j in range(1, n):  # 第i行的第j列
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(m - 1, -1, -1):  # i = 2,1,0
            for j in range(n - 1, 0, -1):  # j = 2,1
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    # 第零列的第i行，或第零行的第i列任一个为零，则将第i行第j列的元素置为零
                    matrix[i][j] = 0
            if hasZeros == 1:
                matrix[i][0] = 0
        return

s = Solution()
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s.setZeroes(matrix)
for line in matrix:
    print(line)