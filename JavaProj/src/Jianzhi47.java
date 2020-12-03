//import java.lang.reflect.Array;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;

public class Jianzhi47 {
    private ArrayList<Integer> createListWithArray(int[]nums){
        ArrayList<Integer> list = new ArrayList<>();
        for (int num : nums){
            list.add(num);
        }
        return list;
    }
    public ArrayList<ArrayList<Integer>> permuteUnique(int[] nums) {
        if (nums.length == 1){
            ArrayList<ArrayList<Integer>> _1 = new ArrayList<>();
            _1.add(createListWithArray(nums));
            return _1;
        }
        else{
            ArrayList<Integer> arraylist = createListWithArray(nums);
            Collections.sort(arraylist);
            int lastVal = arraylist.get(0) - 1;
            ArrayList<ArrayList<Integer>> heheda = new ArrayList<>();
            for (int i = 0; i < arraylist.size(); i++){
                /////////////////////
                if (arraylist.get(i) == lastVal)
                    continue;
                else
                    lastVal = arraylist.get(i);
                /////////////////
                if (i == 0)
                    ArrayList<Integer> otherPart = arraylist.subList(1, arraylist.size()-1);
                else if (i == arraylist.size()-1){

                }

            }
        }
    }
    public static void main(String []args){
        Jianzhi47 s = new Jianzhi47();
        int []nums = new int[]{1, 2, 3};
        s.permuteUnique(nums);

    }
}
