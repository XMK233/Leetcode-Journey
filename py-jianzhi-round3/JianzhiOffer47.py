'''
[剑指 Offer 47. 礼物的最大价值 - 力扣（LeetCode）](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof)

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

 

提示：


	0 < grid.length <= 200
	0 < grid[0].length <= 200

'''
'''
## https://www.pythonheidong.com/blog/article/546114/
## 道理非常简单, 其实就是这里的dp递推原理是: 判断从起点(0, 0)到(i,j)这个点的最大收益是多少.
## 重复一遍, 是从起点开始到某点的最大收益.
### 如果是第一行位置, 那么最大收益只能是从左边来的; 如果是第一列的位置, 那么最大收益只能是从上面来的.
### 如果是其他位置, 那么最大收益就非常简单了, 就是来源于(i-1, j)(i, j - 1)两个位置更大的那个点.
最核心, 这里用的是dp, 不要用dfs, 否则就是自己给自己找罪受. 
'''
class Solution:
    def maxValue(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]

s = Solution()
print((s.maxValue(
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]


)))

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()