/* 88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
*
*
* Solutions:
* The key to solve this problem is moving element of A and B backwards.
* If B has some elements left after A is done, also need to handle that case.
*
* */
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int end = m + n - 1;
        int i = m - 1, j = n - 1;
        for (;i >= 0 && j >= 0; ){
            if (nums1[i] > nums2[j]){
                nums1[end] = nums1[i];
                end -= 1;
                nums1[i] = 0;
                i -= 1;
            }
            else{
                nums1[end] = nums2[j];
                end -= 1;
                nums2[j] = 0;
                j -= 1;
            }
        }
        //------------first revise-----------------
        for (;j >= 0; j--, end--){
            nums1[end] = nums2[j];
        }
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        int a [] = {0};
        int b [] = {1};
        s.merge(a, 0, b, 1);
        for (int i = 0; i < a.length; i++){
            System.out.print(a[i]);
        }
    }
}
