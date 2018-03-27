import java.util.*;

/*
我的思路是分治。
将数组划分为左右两边来进行判别，不断递归，递归到数组只有一个元素的时候就不往下递归了。
此时判断这个数字是不是target，如果是就返回{index， index}，不是就返回{-1, -1}. 
然后递归的上层将下层返回回来的两个数组进行组合，再返回给更上一层，不断类推。

*/

class Solution {
    public int[] merger (int []nums1, int []nums2){
        int [] tmp = new int[2];
        if (nums1[0] == -1 && nums2[0] != -1) tmp[0] = nums2[0];
        else if (nums1[0] != -1 && nums2[0] == -1) tmp[0] = nums1[0];
        else tmp[0] = nums1[0] < nums2[0] ? nums1[0] : nums2[0];

        tmp[1] = Math.max(nums1[1], nums2[1]);

        return tmp;
    }

    public int[] helper(int []nums, int target, int head, int tail){
        if ((tail - head + 1) > 1){
            int [] foreResult = helper(nums, target, head, (head + tail) / 2);
            int [] rearResult = helper(nums, target, (head + tail) / 2 + 1, tail);
            return merger(foreResult, rearResult);
        }

        else{
            if (nums[head] == target){
                int []tmp = {head, head};
                return tmp;
            }
            else {
                int []tmp = {-1, -1};
                return tmp;
            }
        }
    }
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) {
            int []tmp = {-1, -1};
            return tmp;
        }
        return helper(nums, target, 0, nums.length - 1);
    }
}

public class helloworld {
    public static void printString(int [] c){
        for (int i = 0; i < c.length; i++){
            System.out.print(c[i]);System.out.print(" ");
        }
    }
    public static void main(String[] args){
        Solution s = new Solution();

        int b[] = {5, 7, 7, 8, 8, 10};
        int a[] = {4, 5, 6, 0, 1, 2};
        String w[] = {"word", "good", "best", "good"};
        //System.out.println();
        printString(s.searchRange(b, 8));
    }
}
