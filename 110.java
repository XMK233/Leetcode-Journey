import sun.reflect.generics.tree.Tree;
import java.util.*;
import java.util.Collection;

/* 有一个地方自己没意识到：
判断完根节点左右子树高度相差之后，还应该递归
判断左右子树是否分别是平衡的。
* 110. Balanced Binary Tree
Easy

952

86

Favorite

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
*
* */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public int height(TreeNode root){
        if (root == null)
            return 0;
        else{
            return Math.max(height(root.left), height(root.right)) + 1;
        }
    }
    public boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;
        else if (  Math.abs(height(root.left) - height(root.right)) > 1 )
            return false;
        else
            return isBalanced(root.left) && isBalanced(root.right);
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();

        TreeNode t1 = new TreeNode(3);
        TreeNode t2 = new TreeNode(9);
        TreeNode t3 = new TreeNode(20);
        TreeNode t4 = new TreeNode(15);
        TreeNode t5 = new TreeNode(7);

        t1.left = t2;
        t1.right = t3;
        t2.left = null;
        t2.right = null;
        t3.left = t4;
        t3.right = t5;
        t4.left = t4.right = t5.left = t5.right = null;
    }
}
