# https://blog.csdn.net/yangjingjing9/article/details/76910742

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        ### 这个函数的意思是, 从(i, j)出发(不包括这个点), 后续能否找到word这个单词.
        ## 至于递归的方式, 就结合题意, 非常直接地, 上下左右四个方向处理就好. 没什么花活.
        ## 注意, 这个方法里面, 有一个设定操作, 就是设置某一个方位是不是已经访问过了.
        ## 用设置为"#"的方法来反映已经访问过了. 但是记得, 处理完一个路径后, 要把这个井号还原.
        def dfs(x, y, word):
            if len(word) == 0:  # 说明所有字母均在单词板上找到
                return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x - 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # down
            if x < len(board) - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y - 1, word[1:]):
                    return True
                board[x][y] = tmp
            # right
            if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # 首字母相等的位置
                    if (dfs(i, j, word[1:])):  # 寻找下一个字母是否在单词板
                        return True
        return False