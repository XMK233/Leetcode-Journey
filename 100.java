/* 100. Same Tree
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
*
*
* Solutions:
* if p and q are null, return true;
* if they are all not null, only they are the same && their left tree are the same && their right tree
* are the same, can we said that these two tree are the same.
* Otherwise, return false.
*
* */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {

        if (p == q && q == null)
            return true;

        if (p != null && q != null){
            if (p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right))
                return true;
        }

        return false;
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
    }
}
