# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/185a87cd29eb42049132aed873273e83?tpId=117&&tqId=37715&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # def pathSum(self, root: TreeNode, sum: int):
    def sumNumbers(self, root):
        # write code here
        res, path = [], []
        def dfs(node):
            #递归出口：解决子问题
            if not node:
                return #如果没有节点(node = None)，直接返回，不向下执行
            else:               #有节点
                path.append(str(node.val)) #将节点值添加到path
                # sum -= node.val
            # 如果节点为叶子节点，并且 sum == 0
            if not node.left and not node.right:
                res.append(int("".join(path)))

            dfs(node.left) #递归处理左边
            dfs(node.right) #递归处理右边
            path.pop() #处理完一个节点后，恢复初始状态，为node.left,  node.right操作

        dfs(root)
        return sum(res)


def buildTreeFromList(l):
    l_node = []
    for _ in l:
        if _ == "#":
            l_node.append(None)
        else:
            l_node.append(TreeNode(_))
    i = 0
    while i < len(l_node):
        if l_node[i] == None:
            pass
        else:
            if i * 2 + 1 < len(l_node):
                l_node[i].left = l_node[i * 2 + 1]
            if i * 2 + 2 < len(l_node):
                l_node[i].right = l_node[i * 2 + 2]
        i += 1
    return l_node[0]

tree = buildTreeFromList([1, 0])
print(Solution().sumNumbers(tree))