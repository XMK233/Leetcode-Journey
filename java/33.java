import java.util.*;

class Solution {
    public int search(int[] nums, int target) {
        //特殊情况：空数组。
        if (nums.length == 0) return -1;
        int head = 0, tail = nums.length - 1;
        return helper(nums, head, tail, target);
    }
    public int helper (int []nums, int head, int tail, int target){
        //判断头，尾，中是不是目标值：
        if (nums[head] == target) return head;
        if (nums[tail] == target) return tail;

        if (tail == head) return -1;

        //如此取mid，会导致如果待测数组长度为偶数，那么mid的位置是偏左的。
        int mid = (head + tail) / 2;
        if (nums[mid] == target) return mid;
        //头尾中均不是目标值。
        else{
            //如果待测数组不是单调的：
            if (nums[head] > nums[tail]) {
                //mid在前一半递增序列当中
                //mid 有可能是head，因为取mid的机制问题。
                if (nums[mid] >= nums[head]){
                    //如果目标值可能在较大的递增数组中mid的左边的部分的话：
                    if (target < nums[mid] && target > nums[head]) return binarySearch(nums, head, mid, target);
                    //否则就酱紫：
                    else return helper(nums, mid + 1, tail, target);
                }
                //mid在后一半递增序列中
                else {
                    //如果目标值可能在较小的的增数组的mid的右边的部分的话：
                    if (target > nums[mid] && target < nums[tail]) return binarySearch(nums, mid, tail, target);
                    //否则酱紫
                    else return helper(nums, head, mid, target);

                }
            }
            //如果待测数组是单调的：
            else return binarySearch(nums, head, tail, target);
        }
    }

    //普通二分查找法，没用递归。
    public int binarySearch(int []nums, int head, int tail, int target){
        while (head <= tail){
            int mid = (head + tail) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) head = mid + 1;
            else tail = mid - 1;
        }

        return -1;
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int b[] = {0, 1, 2, 3, 4, 5};
        int a[] = {4, 5, 6, 0, 1, 2};
        String w[] = {"word", "good", "best", "good"};
        //System.out.println(s.binarySearhc(b, 0, 5, -1));
        System.out.println(s.search(a, 6));
    }
}
