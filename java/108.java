import sun.reflect.generics.tree.Tree;
import java.util.*;
import java.util.Collection;

/*
思路在于：
中间节点作为当前根节点，左边的递归，右边递归就可以了。
这样建出来的查找二叉树就是平衡的了。
* 108. Convert Sorted Array to Binary Search Tree
Easy

897

95

Favorite

Share
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
*
* */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public TreeNode helper(int[] nums, int left, int right){
        if (left > right)
            return null;
        else if (left == right)
            return new TreeNode(nums[left]);
        else{
            int m = (left + right) / 2;
            TreeNode root = new TreeNode(nums[m]);
            root.left = helper(nums, left, m - 1);
            root.right = helper(nums, m + 1, right);
            return root;
        }
    }
    public TreeNode sortedArrayToBST(int[] nums) {
        return helper(nums, 0, nums.length - 1);
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
