import java.util.HashMap;

public class Jianzhi03 {
    public int findRepeatNumber(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int num: nums){
            Integer itg = Integer.valueOf(num);
            if (!count.containsKey(itg)){
                count.put(itg, 1);
            }
            else {
                return itg.intValue(); //count.put(itg, count.get(itg) + 1);
            }
        }
        return 0;
    }
    public static void main(String []args){
        Jianzhi03 s = new Jianzhi03();
        System.out.println(s.findRepeatNumber(new int[]{2, 3, 1, 0, 2, 5, 3}));
    }
}

/*
* 简单解决了. 直接用哈希.
* 更好的方法见于: https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/yuan-di-zhi-huan-shi-jian-kong-jian-100-by-derrick/
* */