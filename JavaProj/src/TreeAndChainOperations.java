//  Definition for a binary tree node.
class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
 }

public class TreeAndChainOperations {
    public static TreeNode buildTreeFromList(int[] nums){
        TreeNode[] nodes = new TreeNode[nums.length];
        for (int i = 0; i < nums.length; i++){
            nodes[i] = new TreeNode(nums[i]);
        }
        for (int i = 0; i < nums.length; i++){
            if (2 * i + 1 >= nodes.length){
                break;
            }
            nodes[i].left = nodes[2*i+1];
            if (2 * i + 2 >= nodes.length){
                break;
            }
            nodes[i].right = nodes[2*i+2];
        }
        return nodes[0];
    }
}
