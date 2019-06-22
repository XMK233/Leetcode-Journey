/*
 * Essence of this question:
 *
 * if current sum (curSum) is a negative value, then the new subarray will start with the next
 * character.
 * because you want ot find the biggest sum, and the former subarray is negative, why bother adding the former
 * part into your target subarray?
 * */
class Solution{
    public int maxSubArray(int[] nums) {
        int ret = Integer.MIN_VALUE;
        int len = nums.length;
        for (int i = 0, curSum = 0; i < len; i++){
            if (curSum < 0){
                curSum = nums[i];
            }
            else {
                curSum += nums[i];
            }

            if (curSum > ret){
                ret = curSum;
            }
        }

        return ret;
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        int a [] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.print(s.maxSubArray(a));
    }
}
