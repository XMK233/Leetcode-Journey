'''
[剑指 Offer 37. 序列化二叉树 - 力扣（LeetCode）](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof)

请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
'''

'''
参考的这个方法妙啊。
递归方法只要一直处理第一个数字就行了。
这样也少了很多麻烦。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
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
            str1 += self.serialize(root.left)
        else:
            str1 += "#,"
        if root.right:
            str1 += self.serialize(root.right)
        else:
            str1 += "#,"
        return str1

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        list = data.split(",")
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


## https://blog.csdn.net/u010429989/article/details/79266472

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

s = Codec()
print(s.serialize(n1))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


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