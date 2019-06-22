import sun.reflect.generics.tree.Tree;

import java.lang.reflect.Array;
import java.util.*;
import java.util.Collection;

/* reference: https://blog.csdn.net/NoMasp/article/details/50829772
其实道理还是比较简单的。只要后一天的价格比前一天的价格高，总利润就加上这个差值。
最后得到的值就一定是总最高利润。
这题其实有一个潜台词，那就是买入后只能卖出，卖出后只能买入，手头一次只能有一支股票而不能同时手持几支股票。
为什么会是这么做的呢？其实只要想一个连着几天涨价的例子就可以了。比如，【1,2,4,3,1】
我想了想，为什么leetcode网站上给的例子不能让人想到这个解法呢？
因为leetcode给的例子恰好没有连着涨价的情况。都是有涨有跌。
* 122. Best Time to Buy and Sell Stock II
Easy

781

1157

Favorite

Share
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
* */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++){
            if (prices[i] < prices[i + 1]){
                profit += prices[i + 1] - prices[i];
            }
        }
        return profit;
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        int []a = {7,1,5,3,6,4};
        System.out.print(s.maxProfit(a));

        /*TreeNode t1 = new TreeNode(3);
        TreeNode t2 = new TreeNode(9);
        TreeNode t3 = new TreeNode(20);
        TreeNode t4 = new TreeNode(15);
        TreeNode t5 = new TreeNode(7);

        t1.left = t2;
        t1.right = t3;
        t2.left = t4;
        t2.right = t5;
        t3.left = t3.right = t4.left = t4.right = t5.left = t5.right = null;*/

        /*t1.left = t2;
        t1.right = t3;
        t2.left = null;
        t2.right = null;
        t3.left = t4;
        t3.right = t5;
        t4.left = t4.right = t5.left = t5.right = null;*/

    }
}
