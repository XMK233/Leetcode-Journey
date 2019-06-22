import sun.reflect.generics.tree.Tree;

import java.lang.reflect.Array;
import java.util.*;
import java.util.Collection;

/*
* 118. Pascal's Triangle
Easy

563

69

Favorite

Share
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
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
    public List<List<Integer>> generate(int numRows) {
        if (numRows == 0){
            return new ArrayList<List<Integer>>();
        }
        else{
            List<List<Integer>> rst = new ArrayList<List<Integer>>();
            for (int row = 0; row < numRows; row++){
                if (row <= 0){
                    List<Integer> _ = new ArrayList<Integer>();
                    _.add(1);
                    rst.add(_);
                }
                else if (row == 1){
                    List<Integer> _ = new ArrayList<Integer>();
                    _.add(1);_.add(1);
                    rst.add(_);
                }
                else{
                    List<Integer> _ = new ArrayList<Integer>();
                    _.add(1);_.add(1);
                    rst.get(rst.size() - 1);
                    List<Integer> last = rst.get(rst.size() - 1);
                    Integer last_size = last.size();
                    for (int i = 0; i < last_size - 1; i++){
                        Integer sum = last.get(i) + last.get(i + 1);
                        _.add(_.size() - 1 ,sum);
                    }
                    rst.add(_);
                }

            }
            return rst;
        }
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.print(s.generate(0));

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

    }
}
