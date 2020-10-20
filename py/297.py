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
            str1 +=str(root.val)+","
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