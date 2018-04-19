import java.lang.reflect.Array;
import java.util.*;
/*
没有什么太fancy的技巧，就是普通的递归。
先把每一个元素放到数组开头，然后拿后面的数组成新的数组开始进行一波递归。
再把递归回来的东西连上数组开头元素。
应该是谁都能想到的方法。
应该是一种深度优先算法。
* */
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (nums.length == 0)
            ;
        else if (nums.length == 1){
            ret.add(new ArrayList<Integer>(Arrays.asList(nums[0])));
        }
        else if (nums.length == 2){
            ret.add(new ArrayList<Integer>(Arrays.asList(nums[0], nums[1])));
            ret.add(new ArrayList<Integer>(Arrays.asList(nums[1], nums[0])));
        }
        else{
            for (int i = 0; i < nums.length; i++){
                int t = nums[0];
                nums[0] = nums[i];
                nums[i] = t;

                int a[] = new int[nums.length - 1];
                for (int k = 0; k < a.length; k++){
                    a[k] = nums[k + 1];
                }

                List<List<Integer>> subPermutation = permute(a);
                for (int j = 0; j < subPermutation.size(); j++){
                    subPermutation.get(j).add(0, nums[0]);
                }
                ret.addAll(subPermutation);
            }

        }
        return ret;
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int []a = {};
        System.out.print(s.permute(a));
    }
}
