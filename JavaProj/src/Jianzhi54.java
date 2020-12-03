import sun.reflect.generics.tree.Tree;

import java.util.ArrayList;

public class Jianzhi54 {
    public ArrayList<Integer> flattenBST(TreeNode root){
        if (root == null){
            return null;
        }
        else{
            ArrayList<Integer> res = new ArrayList<Integer>();
            // 左子树
            ArrayList<Integer> leftList = flattenBST(root.left);
            if (leftList != null){
                res.addAll(0, leftList);
            }
            // 根节点
            res.add(root.val);
            // 右子树
            ArrayList<Integer> rightList = flattenBST(root.right);
            if (rightList != null){
                res.addAll(res.size(), rightList);
            }
            return res;
        }
    }
    public int kthLargest(TreeNode root, int k) {
        // 展平然后得出结论
        ArrayList<Integer> res = flattenBST(root);
        return res.get(res.size() - k);
    }
    public static void main(String []args){
        Jianzhi54 s = new Jianzhi54();
        TreeNode tn3 = new TreeNode(3);
        TreeNode tn1 = new TreeNode(1);
        TreeNode tn4 = new TreeNode(4);
        TreeNode tn2 = new TreeNode(2);
        tn3.left = tn1;
        tn3.right = tn4;
        tn1.right = tn2;
        System.out.println(s.kthLargest(tn3, 1));
    }
}
