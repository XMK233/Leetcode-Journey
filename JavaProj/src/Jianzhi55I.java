public class Jianzhi55I {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        // 1 加上左右两棵树里面更大的那个深度.
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
