'''
[剑指 Offer 12. 矩阵中的路径 - 力扣（LeetCode）](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof)

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true


示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false


 

提示：


	1 <= board.length <= 200
	1 <= board[i].length <= 200


注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
'''
'''
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 道理非常明了了，就是一个经典的DFS算法。
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            ## 如果出界了，或者当前的board[i][j]不是我想要的word【k】，那就直接GG
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            ## 如果word[k]找到了而且还是最后一个字符，那就找完了，完了事儿了。
            if k == len(word) - 1: return True
            ## 否则就标记当前的board[i][j]已经走过了，不要再回头。
            tmp, board[i][j] = board[i][j], '/'
            ## 然后向四个方向接着寻找
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            ## 这一步也很关键，就是在找后，将棋盘还原，也就是将走过的标记擦除。
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False