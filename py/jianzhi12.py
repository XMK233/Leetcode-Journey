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

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 道理非常明了了，就是一个经典的DFS算法。