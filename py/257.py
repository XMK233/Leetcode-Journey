# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def processList(self, l, val):
        '''
        :param l: l is the list, containing node string
        :param val: val is the root node's value
        :return: processed list l
        '''
        new_l = []
        for ele in l:
            new_l.append("{}->{}".format(val, ele))
        return new_l

    def binaryTreePaths(self, root):
        ## 边界条件
        if root == None:
            return []
        ## 普通情况
        ###最基本情况: root就是叶节点.
        if root.left == None and root.right == None:
            return ['{}'.format(root.val)]
        ### 对左右节点送上来的路径表进行处理以及合并
        else:
            left_list = self.processList(self.binaryTreePaths(root.left), root.val)
            right_list = self.processList(self.binaryTreePaths(root.right), root.val)
            left_list.extend(right_list)
            return left_list

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n5 = TreeNode(5)
# n1.left = n2
# n1.right = n3
# n2.right = n5

n1 = None # TreeNode(1)

s = Solution()
print(s.binaryTreePaths(n1))