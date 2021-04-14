# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/f31fc6d3caf24e7f8b4deb5cd9b5fa97?tpId=117&&tqId=37822&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

参考题解:
递归套路，主要是分解信息和合并左右子树需要提供的信息。
当前节点是完全二叉树条件：


或者其他思路,
二叉搜索树:
    判断二叉搜索树的条件是中序遍历后看是否是递增的序列,
    xx当前节点是二叉搜索树条件：左右子树都为搜索树 且 左树根节点值及其根节点右节点都小于当前节点。右树同理. ## 这个思路是有误的, 找一个例子就能攻破. 5, 2, #, 1, 4, #, #, 0, 1.5, 3, 7, #,#,#,#
    判断当前节点是不是搜索树, 那么就要判断当前节点的值是不是介于理论上下限之间; 如果是, 递归判断左子节点是不是介于理论下限和父节点值之间, 右子节点的值是不是介于父节点值和理论上限之间即可.
完全二叉树:
    完全二叉树的条件是按层遍历, 如果遇上空节点而且后续全是空节点, 就是完全二叉树.
    xx左子树为完全二叉树 右子树也为完全二叉树 且 左树为空时右树必须为空. ## 这个思路不行. 找一个反例: 1, 2, 3, 4, #, 5, 6
'''

class Solution:
    def judgeIt(self , root ):
        if not root:
            return True, True
        return self.isValidBST(root), self.full(root)

    def isValidBST(self, root):
        ## 判断当前节点是不是搜索树, 那么就要判断当前节点的值是不是介于理论上下限之间; 如果是, 递归判断左子节点是不是介于理论下限和父节点值之间, 右子节点的值是不是介于父节点值和理论上限之间即可.
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, min, max):
        if not root: return True
        if root.val >= max or root.val <= min:
            return False
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)

    def full(self, node):
        if not node: return True
        queue = [node]
        while len(queue) > 0 and queue[0]: ## queue有节点且不为空节点
            t = queue.pop(0)
            queue.append(t.left)
            queue.append(t.right)
        while len(queue) > 0:
            if queue[0] == None:
                queue.pop(0)
            else:
                break
        return len(queue) == 0


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

two = buildTreeFromList([2, 1, 4, 0, 1.5, 3, 7])
five = TreeNode(5)
five.left = two
s = Solution()
print(s.judgeIt(five))