'''
[面试题 17.23. 最大黑方阵 - 力扣（LeetCode）](https://leetcode-cn.com/problems/max-black-square-lcci)

给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。

示例 1:

输入:
[
   [1,0,1],
   [0,0,1],
   [0,0,1]
]
输出: [1,0,2]
解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵


示例 2:

输入:
[
   [0,1,1],
   [1,0,1],
   [1,1,0]
]
输出: [0,0,1]


提示：


	matrix.length == matrix[0].length <= 200

'''

from collections import defaultdict
class Solution:
    def findSquare(self, matrix):
        if not matrix:
            return []
        maxRight = [[0] * len(matrix[0]) for i in range(len(matrix))]
        maxDown = [[0] * len(matrix[0]) for i in range(len(matrix))]
        ## 从右下遍历到左上：
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] == 0:
                    ## 如果当前值是0，也就意味着至少有1咯。
                    if j == len(matrix[0]) - 1:
                        ## 特殊情况，也就是最后一列。
                        maxRight[i][j] = 1
                    else:
                        maxRight[i][j] = maxRight[i][j + 1] + 1
                    if i == len(matrix) - 1:
                        ## 特殊情况，也就是最后一行。
                        maxDown[i][j] = 1
                    else:
                        maxDown[i][j] = maxDown[i + 1][j] + 1
                else:
                    ## 如果当前值不为0，那么无论这个位置的右边和下面有多少个0，都白搭。
                    maxRight[i][j] = 0
                    maxDown[i][j] = 0
                # print(i, j, maxRight[i][j], maxDown[i][j])
        res = []
        ## 再度遍历，从左上往右下
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    continue
                ## 最长的可能边长也就是如下行。实际可能还短。
                maxPossible = min(maxRight[i][j], maxDown[i][j])
                ## 按照长度递减的方式，来检查所有的可能长度
                for l in range(maxPossible, 0, -1):
                    # print(maxPossible, l)
                    if maxDown[i][j + l - 1] >= l and maxRight[i + l - 1][j] >= l:
                        if not res: ## 如果此时res还是空的，那就要放进第一个答案。
                            res.extend([i, j, l])
                        else:## 如果此时res不是空的，就要和之前的答案进行对比
                            if l > res[-1]: ## 如果比之前的要大，就更新答案
                                res = [i, j, l]

        return res

    def findSquare_ref(self, matrix):
        ### 这是参考的方法.
        if not matrix:
            return []
        mxHorizontal = defaultdict(int)
        mxVertical = defaultdict(int)
        rows, cols = len(matrix), len(matrix[0])
        res = []
        ## 这里的两重循环是通过动态规划的思维来填充两个defaultdict.
        ## 这俩dict有什么用呢: 记载了从(r,c)这个点开始, 往右或者往下最长的黑边分别有多长.
        ## 注意啊, 这里两个dict相当于是反着填充的, 你看到没, 方阵是反着遍历的.
        for r in range(rows)[::-1]:
            for c in range(cols)[::-1]:
                if matrix[r][c] == 0:
                    mxHorizontal[r, c] = 1 + mxHorizontal[r, c + 1]
                    mxVertical[r, c] = 1 + mxVertical[r + 1, c]
        ## 然后就是正着遍历方阵.
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    mxsize = min(mxHorizontal[r, c], mxVertical[r, c])
                    cursize = 0 if not res else res[2]
                    for size in range(mxsize, cursize, -1):
                        if mxVertical[r, c + size - 1] >= size and mxHorizontal[r + size - 1, c] >= size:
                            ## 这个if语句是什么意思? 我想了蛮久的，终于给我想出来了。
                            ### 从(r, c)出发, 往右和往下最长的黑边, 为mxsize. 这两个方向是确定OK的。
                            ### 那么, 当我们确定了(r,c)也就是左上角OK了, 是不是要进一步确认一下右上角(r, c + size - 1)往下、以及
                            ### 左下角（r + size - 1, c）往右也符合规定？
                            ### 这就是这个if语句的用意。
                            ### 而且这个if语句是从mxsize开始倒着遍历的。也就是从最大的可能边长开始倒着遍历。
                            ### 如果mxsize比cursize小，那就不遍历了。
                            res = [r, c, size]
                            break
        return res

s = Solution()
print(s.findSquare(
[
   [1,1,0],
]

))

# 作者：suibianfahui
# 链接：https://leetcode-cn.com/problems/max-black-square-lcci/solution/20xing-dai-ma-by-suibianfahui/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。