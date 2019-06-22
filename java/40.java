/*
参考了这个人的解法： https://blog.csdn.net/u012848330/article/details/52187549 
遇到了坑：注意要把某些地方已经入数组的部分去除。也只有这样，才能够满足回溯的条件。
*/

import java.util.*;

class Solution {
    public void helper (int[] candidates, int index, int target, List<Integer> list, List<List<Integer>> ret){
        for (int i = index; i < candidates.length; i++){
            int temp = candidates[i];
            if (temp == target){
                list.add(temp);
                ret.add(new ArrayList<Integer>(list));
                list.remove(list.size() - 1);
                return;
            }
            else if (temp < target){
                list.add(temp);
                int tmpLength = list.size();
                helper(candidates, i + 1, target - temp, list, ret);
                list = list.subList(0, tmpLength - 1);
                while (i + 1 < candidates.length && candidates[i] == candidates[i + 1])
                    i++;
            }
            else
                return;
        }

    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        int index = 0;

        Arrays.sort(candidates);
        helper(candidates, index, target, list, ret);

        return ret;

    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int []a = {1, 1, 1, 1, 2};
        System.out.print(s.combinationSum2(a, 3));
    }
}
