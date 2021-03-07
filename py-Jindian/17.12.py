'''
[面试题 17.12. BiNode - 力扣（LeetCode）](https://leetcode-cn.com/problems/binode-lcci)

二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

注意：本题相对原题稍作改动

 

示例：

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]


提示：


	节点数量不会超过 100000。

方法很简单, 就是直接进行递归嘛. 然后每一轮递归都返回两个值, 也就是头节点和尾节点的指针.
其他的很容易也很简单.
发现自己的工程实现能力却有不行.

'''

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def helper(root):
            #############
            if root is None: return None, None
            #############
            if root.left == None:
                leftHead, leftTail = root, root ## 这里之前写出了语法错误. 注意, 为两个变量赋值, 要写成这种形式哦.
            else:
                leftHead, leftTail = helper(root.left)
                leftTail.right = root
            #############3
            if root.right == None:
                rightHead, rightTail = root, root
            else:
                rightHead, rightTail = helper(root.right)
                root.right = rightHead
            #################
            root.left = None
            return leftHead, rightTail

        if root is None: return None
        newHead, newTail = helper(root)
        return newHead

node4 = TreeNode(4)
node2 = TreeNode(2)
node5 = TreeNode(5)
node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node0 = TreeNode(0)
node4.left = node2
node4.right = node5
node2.left = node1
node2.right = node3
node1.left = node0
node5.right = node6

a = Solution().convertBiNode(node4)
print()

