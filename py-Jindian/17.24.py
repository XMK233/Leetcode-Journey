'''
[面试题 17.24. 最大子矩阵 - 力扣（LeetCode）](https://leetcode-cn.com/problems/max-submatrix-lcci)

给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

注意：本题相对书上原题稍作改动

示例：

输入：
[
   [-1,0],
   [0,-1]
]
输出：[0,1,0,1]
解释：输入中标粗的元素即为输出所表示的矩阵

 

说明：


	1 <= matrix.length, matrix[0].length <= 200

'''
'''
### https://leetcode-cn.com/problems/max-submatrix-lcci/solution/zhe-yao-cong-zui-da-zi-xu-he-shuo-qi-you-jian-dao-/
有一个核心的操作, 就是假定这会子研究的矩阵是a*b维的, 那么我们就把每一列的值给它加起来, 降成1维的, 再做dp, 就会打开新世界大门. 
'''
class Solution:
    def getMaxMatrix(self, matrix):
        ## 这个方法是我根据参考的教程, 自己实现的.
        N = len(matrix) ## 行数
        M = len(matrix[0]) ## 列数
        ans = [0] * 4 ## 最后的结果数组, 记录左上角的行列, 以及右下角的行列值.
        maxDp = float("-Inf") ## 该值用以记载最大的矩阵和. 该值初始化为最小的数字.
        for i in range(N): ## 遍历行
            colSums = [0] * M ## 记载列的和
            topLeftCol = 0 ## 记载左上角点的列数.
            for j in range(i, N): ## 二重循环遍历行. 这一步体现了子矩阵的构造: 这个子矩阵始于第i行, 终于第j行.
                dp = 0 ## 这里犯了个错. dp为0应该放在第二重循环里面, 而非第一重循环.
                for k in range(M): ## 遍历列
                    colSums[k] += matrix[j][k] ### 求列和
                    if dp <= 0:
                        dp = colSums[k]
                        topLeftCol = k
                    else:
                        dp += colSums[k]
                    if dp > maxDp:
                        maxDp = dp
                        ans[0] = i
                        ans[1] = topLeftCol
                        ans[2] = j
                        ans[3] = k
        return ans