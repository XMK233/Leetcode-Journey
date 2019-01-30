import sun.reflect.generics.tree.Tree;

import java.lang.reflect.Array;
import java.util.*;
import java.util.Collection;

/* 这道题的解法其实是有技巧的。是可以找规律的。
但是这里我还是只用了最基础的方法，其实就是118题的简化版。所以得到的结果时空复杂度较高。
公式可参考 https://blog.csdn.net/NoMasp/article/details/50568802
* 119. Pascal's Triangle II
Easy

394

149

Favorite

Share
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
*
* */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> getRow(int rowIndex) {
        if (rowIndex < 0){
            return new ArrayList<Integer>();
        }
        else {
            List<List<Integer>> rst = new ArrayList<List<Integer>>();
            int numRows = rowIndex + 1;
            for (int row = 0; row < numRows; row++){
                if (row <= 0){
                    List<Integer> _ = new ArrayList<Integer>();
                    _.add(1);
                    rst.add(_);
                }
                else if (row == 1){
                    rst.remove(0);
                    List<Integer> _ = new ArrayList<Integer>();
                    _.add(1);_.add(1);
                    rst.add(_);
                }
                else{
                    List<Integer> _ = new ArrayList<Integer>();
                    _.add(1);_.add(1);
                    List<Integer> last = rst.get(rst.size() - 1);
                    rst.remove(last);
                    Integer last_size = last.size();
                    for (int i = 0; i < last_size - 1; i++){
                        Integer sum = last.get(i) + last.get(i + 1);
                        _.add(_.size() - 1 ,sum);
                    }
                    rst.add(_);
                }

            }
            return rst.get(0);
        }
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.print(s.getRow(0));

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
