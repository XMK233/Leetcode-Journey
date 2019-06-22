import sun.reflect.generics.tree.Tree;

import java.lang.reflect.Array;
import java.util.*;
import java.util.Collection;

/* reference: https://blog.csdn.net/DERRANTCM/article/details/47651235
* 121. Best Time to Buy and Sell Stock
Easy

2059

103

Favorite

Share
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Accepted
414,388
Submissions
906,639
*
* */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 0)
            return 0;
        else{
            int profit = 0;
            int min = prices[0];
            for (int i = 1; i < prices.length; i++){
                if (prices[i] <= min){
                    min = prices[i];
                }
                else{
                    int newProfit =  prices[i] - min;
                    if (newProfit > profit)
                        profit = newProfit;
                }
            }
            return profit;
        }
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        //System.out.print(s.maxProfit(0));

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
