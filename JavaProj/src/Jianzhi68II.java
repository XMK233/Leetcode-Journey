/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

//class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;
//     TreeNode(int x) { val = x; }
//}

public class Jianzhi68II {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // 思路是什么?
        // 如果root就是要找的某一个点, 或者是null, 直接返回root即可.
        if (root == p || root == q || root == null){
            return root;
        }

        // 去左子树和右子树分别去找两个目标点.
        TreeNode leftAncester = this.lowestCommonAncestor(root.left, p, q);
        TreeNode rightAncester = this.lowestCommonAncestor(root.right, p, q);

        // 如果两边各能找到一个点, 那么root就是他们的最近祖先.
        if (leftAncester != null && rightAncester != null){
            return root;
        }

        // 否则, 那棵子树得到的最近祖先就是最后返回值.
        if (leftAncester != null){
            return leftAncester;
        }

        return rightAncester;
    }

}
