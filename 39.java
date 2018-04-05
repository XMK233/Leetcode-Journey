import java.util.*;

class Solution {
    public boolean isTheSame(List<Integer> a, List<Integer> b){
        for (int k = 0; k < a.size(); k++){
            if (a.get(k) != b.get(k))
                return false;
        }
        return true;
    }

    public boolean isIn(List<Integer> list, List<List<Integer>> pool){
        for (int i = 0; i < pool.size(); i++){
            if (list.size() == pool.get(i).size() && isTheSame(list, pool.get(i)))
                return true;
        }
        return false;
    }

    public void addAllWithoutDuplication(List<List<Integer>> a, List<List<Integer>> b){
        if (a.size() == 0){
            a.addAll(b);
            return;
        }
        //
        List<List<Integer>> newPart = new ArrayList<List<Integer>>();
        for (List<Integer> i : b){
            if (!isIn(i, a))
                a.add(i);
        }
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> out = new ArrayList<List<Integer>>();

        for (int i = 0; i < candidates.length; i++){
            int curNum = candidates[i];

            //current number larger than target
            if (curNum > target)
                continue;

            //current number is equal to the target
            if (curNum == target){
                List<Integer> tmpSub = new ArrayList<Integer>();
                tmpSub.add(curNum);
                out.add(tmpSub);
                continue;
            }

            //current number is less than target
            int counter = target - curNum;
            List<List<Integer>> tmp = combinationSum(candidates, counter);

            if (tmp.size() == 0) continue;
            else{
                for (List<Integer> j : tmp){
                    j.add(curNum);
                    Collections.sort(j);
                }
                //out.addAll(tmp);
                addAllWithoutDuplication(out, tmp);
            }
        }

        return out;
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int []a = {1, 2};
        System.out.print(s.combinationSum(a, 3));
    }
}
