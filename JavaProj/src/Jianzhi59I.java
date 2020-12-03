import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class Jianzhi59I {
    public int[] maxSlidingWindow(int[] nums, int k) {
//        int [] resList = new int[nums.length];
        ArrayList<Integer> resList = new ArrayList<Integer>();
        Deque<Integer> indexDeque = new LinkedList<Integer>();
        int maxIndex = -1;
        for (int i = 0; i < nums.length; i++){
            // 先更新各种表啊队列啊什么的
            if (indexDeque.isEmpty()){
                indexDeque.add(i);
            }
            else{
                // 先看当前的最大值index是否过期. 如果过期了就要删掉
                if (i - indexDeque.element() >= k){
                    indexDeque.removeFirst();
                }
                // 然后接着处理.
                while (!indexDeque.isEmpty()){
                    int lastIndex = indexDeque.removeLast();
                    if (nums[i] <= nums[lastIndex]) {
                        indexDeque.add(lastIndex);
                        break;
                    }
                }
                indexDeque.add(i);
            }
            //然后, 就可以更新结果列表了. 注意, 要遍历到一定长度才能弄
            if (i >= k - 1){
                resList.add(nums[indexDeque.element()]);
            }
        }
        // 生成最后返回的结果.
        // 艹, 真jb麻烦, 人生苦短, 干嘛不用py?
        int [] res = new int[resList.size()];
        for (int i = 0; i < resList.size(); i++){
            res[i] = resList.get(i);
        }
        return res;
    }

    public static void main(String []args){
        Jianzhi59I s = new Jianzhi59I();
        int [] res = new int[]{1,3,-1,-3,5,3,6,7};
        System.out.println(Arrays.toString(s.maxSlidingWindow(res, 3)));
    }
}
