# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?tpId=117&&tqId=37782&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树
示例1
输入
复制
{8,6,10,5,7,9,11}
返回值
复制
{8,6,10,5,7,9,11}

剑指offer37
我参考的这个题解的关键在哪里你晓得嘛?
就是如果遇到None的, 就在对应位置上放一个"#"字符, 哪怕是叶子节点的左右两个节点都是空节点,
也得放俩"#"在对应位置.
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def Serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        str1 = ""
        if root is None:
            return "#"
        else:
            str1 += str(root.val) + ","
        if root.left:
            str1 += self.Serialize(root.left)
        else:
            str1 += "#,"
        if root.right:
            str1 += self.Serialize(root.right)
        else:
            str1 += "#,"
        return str1

    def Deserialize(self, s):
        # write code here
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        list = s.split(",")
        if list == []:
            return None
        if list[-1] == "":
            list.pop(-1)
        return self.deserialize_(list)

    def deserialize_(self, list):
        if list[0] == '#':
            list.pop(0)
            return None
        root = TreeNode(int(list[0]))
        list.pop(0)
        root.left = self.deserialize_(list)
        root.right = self.deserialize_(list)
        return root