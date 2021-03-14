# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=117&&tqId=37759&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
#-*- coding:utf-8 -*-

## 把二叉查找树变为排序双向链表
## 这个思路非常直白，就是按照中序遍历，把二叉查找树压平成节点数组，
## 然后把数组里面已经排序好的节点连起来就好啦。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def zhongxu(self,root):
        if not root:
            return []
        return self.zhongxu(root.left)+[root]+self.zhongxu(root.right)
    def Convert(self, pRootOfTree):
        # write code here
        list1=self.zhongxu(pRootOfTree)
        if len(list1)==0:
            return None
        if len(list1)==1:
            return pRootOfTree
        for i in range(len(list1)-1):
            list1[i].right=list1[i+1]
            list1[i+1].left=list1[i]
        return list1[0]