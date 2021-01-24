'''
[剑指 Offer 34. 二叉树中和为某一值的路径 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof)

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1


返回:

[
   [5,4,11,2],
   [5,8,4,5]
]


 

提示：


	节点总数 <= 10000


注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/
'''

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