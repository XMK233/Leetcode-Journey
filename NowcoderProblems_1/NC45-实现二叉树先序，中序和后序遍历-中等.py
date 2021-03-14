# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/a9fec6c46a684ad5a3abd4e365a9d362?tpId=117&&tqId=37819&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
分别按照二叉树先序，中序和后序打印所有的节点。
示例1
输入
复制
{1,2,3}
返回值
复制
[[1,2,3],[2,1,3],[2,3,1]]
备注:
n \leq 10^6n≤10
6

这个方法，能够将三种遍历方式全部过一遍，很6的。要好好学学。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self, root):
        # write code here
        pre_order, in_order, post_order = [], [], []

        def find(root):
            if not root:
                return None
            pre_order.append(root.val)
            find(root.left)
            in_order.append(root.val)
            find(root.right)
            post_order.append(root.val)

        find(root)
        return [pre_order, in_order, post_order]