class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False

# https://blog.csdn.net/fuxuemingzhu/article/details/79459314
## 技巧其实非常简单，就是从右上角或者左下角出发来找。
## 你只要用例子来找找看，就发现，诶，上述找法是对的。擦勒。