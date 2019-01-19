import sun.reflect.generics.tree.Tree;
import java.util.*;
import java.util.Collection;

/*
* Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
* (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
* 
* */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        Queue<Integer> levelQueue = new LinkedList<>();
        ArrayList<Integer> level = new ArrayList<>();
        ArrayList<List<Integer>> levels = new ArrayList<List<Integer>>();
        nodeQueue.offer(root);
        levelQueue.offer(1);
        //ArrayList<Integer> cur_level = new ArrayList<>();
        int cur_level = 1;
        for (; !nodeQueue.isEmpty(); ){
            TreeNode nd = nodeQueue.poll();
            Integer nd_lvl = levelQueue.poll();

            if (cur_level == nd_lvl) { //不用换行
                ;
            }
            else {//需要换行了
                levels.add(level);
                level = new ArrayList<>();
                cur_level = nd_lvl;
            }
            if (nd != null) {
                level.add(nd.val);
                nodeQueue.offer(nd.left);
                levelQueue.offer(nd_lvl + 1);
                nodeQueue.offer(nd.right);
                levelQueue.offer(nd_lvl + 1);
            }

        }
        Collections.reverse(levels);
        return levels;
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
        System.out.print(s.levelOrderBottom(t1));

    }
}
