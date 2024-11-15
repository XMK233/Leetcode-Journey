#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self , matrix) -> int:
        # write code here
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    pass
                elif i == 0 and j != 0:
                    matrix[i][j] = matrix[i][j-1] + matrix[i][j]
                elif i != 0 and j == 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j]
                else:
                    matrix[i][j] = min(
                        matrix[i - 1][j], matrix[i][j-1]
                    ) + matrix[i][j]
        return matrix[i][j]

s = Solution()
print(s.minPathSum(
    [[1,2,3],[1,2,3]]
))