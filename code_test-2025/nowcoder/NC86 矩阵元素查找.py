# -*- coding:utf-8 -*-
'''
反正要义就是一个，就是从左下开始往右上去找。如果待查值大于当前值，就往右走，否则就往上走。
我感觉好像未必不能从右下往左上去找，就是非常麻烦。
如果不用这样的，也可以用简单直观的：逐行去看，首先判断一下当前值会不会不在这一行。然后找到所在行之后再去找具体的列，就得了。
'''
class Solution:
    def findElement(self, mat, n, m, x):
        matrix = mat
        target = x
        ## 这个i,j就说明了, 我们从左下角开始的.
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if matrix[i][j] == target:
                return [i, j]#True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return []# False