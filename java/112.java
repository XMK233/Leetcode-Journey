import sun.reflect.generics.tree.Tree;
import java.util.*;
import java.util.Collection;

/* 
* 112. Path Sum
Easy

733

237

Favorite

Share
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null)
            return false;
        //
        boolean left_haPath = false, right_hasPath = false, cur_isTarget = false;
        if (root.left != null)
            left_haPath = hasPathSum(root.left, sum - root.val);
        if (root.right != null)
            right_hasPath = hasPathSum(root.right, sum - root.val);
        if (root.left == null && root.right == null)
            cur_isTarget = root.val == sum;
        return (left_haPath | right_hasPath | cur_isTarget);
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
