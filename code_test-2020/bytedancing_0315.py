# coding=utf-8

## 题目就是, 给你一个9*9二维数组, 里面填1-9的数字, 然后不是数字的地方填".", 问你, 这个二维数组是不是一个有效的数独.
## 直接暴力求解. 面试官的意思是啊, 判断九宫格编号的函数jiugongge_id()写的不够优雅.

## 其实就是力扣第36题. 以下是当时写的代码, 性能上至少在力扣是打败了8成以上的用户. 但是对面试官来说还是不满意. 

def isValidSudoku(table):
    """
    :type table: List[List[str]]
    :rtype: bool
    # 要求：每个元素只能遍历一次
    """

    def jiugongge_id(i, j):
        if (i >= 0 and i <= 2) and (j >= 0 and j <= 2):
            return 0
        if (i >= 0 and i <= 2) and (j >= 3 and j <= 5):
            return 1
        if (i >= 0 and i <= 2) and (j >= 6 and j <= 8):
            return 2

        if (i >= 3 and i <= 5) and (j >= 0 and j <= 2):
            return 3
        if (i >= 3 and i <= 5) and (j >= 3 and j <= 5):
            return 4
        if (i >= 3 and i <= 5) and (j >= 6 and j <= 8):
            return 5

        if (i >= 6 and i <= 8) and (j >= 0 and j <= 2):
            return 6
        if (i >= 6 and i <= 8) and (j >= 3 and j <= 5):
            return 7
        if (i >= 6 and i <= 8) and (j >= 6 and j <= 8):
            return 8

    lines = [[] for i in range(9)]
    cols = [[] for i in range(9)]
    nines = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            num = table[i][j]
            if num == ".":
                continue
            ## lines:
            if num in lines[i]:
                return False
            else:
                lines[i].append(num)
            ## cols:
            if num in cols[j]:
                return False
            else:
                cols[j].append(num)
            ## nines
            nine_id = jiugongge_id(i, j)
            if num in nines[nine_id]:
                return False
            else:
                nines[nine_id].append(num)

    return True
