# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/7298353c24cc42e3bd5f0e0bd3d1d759?tpId=117&&tqId=37841&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
已知两颗二叉树，将它们合并成一颗二叉树。合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替。例如：
两颗二叉树是:
Tree 1
     1
    / \
   3   2
  /
 5

Tree 2
   2
  / \
 1   3
  \   \
   4   7

合并后的树为
    3
   / \
  4   5
 / \    \
5  4    7
示例1
输入
复制
{1,3,2,5},{2,1,3,#,4,#,7}
返回值
复制
{3,4,5,5,4,#,7}
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param t1 TreeNode类
# @param t2 TreeNode类
# @return TreeNode类
#

## 道理，看了代码就自然懂了。直接掌声。
class Solution:
    def mergeTrees(self , t1 , t2 ):
        # write code here
        if t1 == None: return t2
        if t2 == None: return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1