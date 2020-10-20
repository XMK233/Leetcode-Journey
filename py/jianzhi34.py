class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(node, sum):
            #递归出口：解决子问题
            if not node: return #如果没有节点(node = None)，直接返回，不向下执行
            else:               #有节点
                path.append(node.val) #将节点值添加到path
                sum -= node.val
            # 如果节点为叶子节点，并且 sum == 0
            if not node.left and not node.right and not sum:
                res.append(path[:])

            dfs(node.left, sum) #递归处理左边
            dfs(node.right, sum) #递归处理右边
            path.pop() #处理完一个节点后，恢复初始状态，为node.left,  node.right操作

        dfs(root, sum)
        return res

# 作者：xilepeng
# 链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/dfs-jian-dan-yi-dong-by-xilepeng/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 好好学习一下人家的实现方式. 很好的.