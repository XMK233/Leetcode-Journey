public class Jianzhi68I {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // 如果root自己就是要找的其中一个点, 直接将其返回即可.
        if (root == p || root == q || root == null){
            return root;
        }
        // 如果一大一小于root, 直接返回root;
        if (root.val > p.val && root.val < q.val || root.val < p.val && root.val > q.val){
            return root;
        }
        // 如果二者皆大于或者小于root, 那就去相应子树递归寻找;
        if (p.val > root.val && q.val > root.val){
            return this.lowestCommonAncestor(root.right, p, q);
        }
        if (p.val < root.val && q.val < root.val){
            return this.lowestCommonAncestor(root.left, p, q);
        }
        // wow.
        return null;
    }
}
