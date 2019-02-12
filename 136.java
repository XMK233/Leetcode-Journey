/*
reference: 
https://blog.csdn.net/Cloudox_/article/details/52459584

What you can do is to ^ all the numbers. 

2 same numbers will get 0 when doing ^;
numbers other than 0 ^ 0 will get number other than 0;
^ is not violating the commutative law;


136. Single Number
Easy

2020

80

Favorite

Share
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

*/

class Solution {
    public int singleNumber(int[] nums) {
        int t = 0;
        for (int i = 0; i < nums.length; i++){
            t ^= nums[i];
        }
        return t;
    }   
}