public class Jianzhi55II {
    public int depthOfTree(TreeNode root){
        if (root == null)
            return 0;
        else
            return 1 + Math.max(
                    depthOfTree(root.left),
                    depthOfTree(root.right)
            );
    }
    public boolean isBalanced_helper(TreeNode root){
        if (root == null)
            return true;
        // 如果左右两棵树有一个不是平衡的, 那就直接GG.
        if (!(isBalanced_helper(root.left) && isBalanced_helper(root.right))) return false;
        // 如果两者皆平衡, 然后就看深度
        int depthLeft = depthOfTree(root.left);
        int depthRight = depthOfTree(root.right);
        // 如果深度差很大, 直接GG
        if (Math.abs(depthLeft - depthRight) > 1) return false;
        // 差不多, 就OK.
        return true;
    }
    public boolean isBalanced(TreeNode root) {
        // 基本思路: 左边是平衡的, 右边是平衡的, 并且两边的深度是一样的.
        return isBalanced_helper(root);
    }

}
