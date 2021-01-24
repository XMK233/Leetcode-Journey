'''
[剑指 Offer 27. 二叉树的镜像 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof)

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]


 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/
'''

'''
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/solution/mian-shi-ti-27-er-cha-shu-de-jing-xiang-di-gui-fu-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 其实很简单了，直接抄。
## 就是单纯的把左右边给它换过来，然后分别镜像即可。
'''

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
