import java.util.*;
/*
思路比较简单，也就是二分查找，递归，然后到数组只有两个数字为止。
然后查一下这两个数字是不是我们要找的数字，是就返回index，不是的话就找它应该插在哪里。
*/
class Solution {
    public int helper(int []nums, int target, int head, int tail){
        if ((tail - head) > 1 ) {
            int mid = (tail + head) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] > target) return helper(nums, target, head, mid - 1);
            else return helper(nums, target, mid + 1, tail);
        }
        else{
            if (nums[head] == target) return head;
            else if (nums[tail] == target) return tail;
            else {
                if (target < nums[head]) return head;
                else if (target > nums[tail]) return tail + 1;
                else return tail;
            }
        }
    }

    public int searchInsert(int[] nums, int target) {
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

        int a[] = {1, 3, 5, 6};
        String w[] = {"word", "good", "best", "good"};
        System.out.println(s.searchInsert(a, 7));
    }
}
