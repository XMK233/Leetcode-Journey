import sun.reflect.generics.tree.Tree;
import java.util.*;
import java.util.Collection;

/* 脑子秀逗了，判断两边是不是都是空的时候竟然都写不对。
* 111. Minimum Depth of Binary Tree
Easy

594

299

Favorite

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
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

    public int minDepth(TreeNode root) {
        if (root == null)
            return 0;
        else if (root.left == null && root.right == null){
            return 1;
        }
        else if (root.left != null && root.right != null){
            return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
        }
        else { //if ((root.left == null && root.right != null) || (root.right == null && root.left != null))
            return root.left != null ? minDepth(root.left) + 1 : minDepth(root.right) + 1;
        }
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
        t2.left = t4;
        t2.right = t5;
        t3.left = t3.right = t4.left = t4.right = t5.left = t5.right = null;

        /*t1.left = t2;
        t1.right = t3;
        t2.left = null;
        t2.right = null;
        t3.left = t4;
        t3.right = t5;
        t4.left = t4.right = t5.left = t5.right = null;*/
        System.out.print(s.minDepth(t1));

    }
}
