class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ## 基本想法: 将海湾全部标记出来, 然后统一填湖.
    ## https://blog.csdn.net/danspace1/article/details/88010210
    ## 思路借鉴的别人, 但是设计实现是自己弄的.
    def bfs(self, board):
        return

    def dfs(self, location, board):
        ### location: (i, j)
        numCol = len(board[0])
        numRow = len(board)
        for direction in self.directions:
            newLocation = (location[0] + direction[0], location[1] + direction[1])
            ## 不越界并且找到了一片联通的水域
            if (0 <= newLocation[0] <= numRow - 1 and 0 <= newLocation[1] <= numCol - 1) and board[newLocation[0]][newLocation[1]] == "O":
                board[newLocation[0]][newLocation[1]] = "A"
                self.dfs(newLocation, board)
        return

    def solve(self, board) -> None:
        ## 空盘, 直接不处理了.
        ###
        numRow = len(board)
        if numRow == 0:
            return
        numCol = len(board[0])
        if numCol == 0:
            return
        ### 第一行
        for j in range(numCol):
            ## 发现入海口, 开始探索海湾边界
            if board[0][j] == "O":
                board[0][j] = "A"
                self.dfs((0, j), board)
        ### 最后一列
        for i in range(numRow):
            if board[i][numCol - 1] == "O":
                board[i][numCol - 1] = "A"
                self.dfs((i, numCol - 1), board)
        ### 最后一行
        for j in range(numCol):
            if board[numRow - 1][j] == "O":
                board[numRow - 1][j] = "A"
                self.dfs((numRow - 1, j), board)
        ### 第一列
        for i in range(numRow):
            if board[i][0] == "O":
                board[i][0] = "A"
                self.dfs((i, 0), board)
        #####
        ## 上述步骤完事后, 海湾就算探索完毕了.
        ## 现在开始填湖. 
        for i in range(numRow):
            for j in range(numCol):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
        return

s = Solution()
board = [
    ["X", "X", "X", "X", "O", "O", "X", "X", "X", "X"],
    ["X", "O", "O", "X", "X", "O", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "X", "O", "X", "O", "O", "O"],
    ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
    ["X", "X", "X", "X", "X", "O", "X", "O", "O", "X"],
    ["O", "O", "O", "X", "X", "O", "X", "O", "X", "X"],
    ["X", "X", "O", "X", "O", "X", "X", "O", "X", "X"],
    ["X", "O", "O", "X", "O", "X", "X", "O", "X", "X"],
    ["X", "X", "X", "X", "O", "X", "X", "O", "X", "X"],
    ["X", "O", "O", "X", "O", "X", "X", "O", "X", "X"],
]
# board = [["O"]]
board = []
s.solve(board)
for row in board:
    print(row)

