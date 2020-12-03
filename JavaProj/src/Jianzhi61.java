import java.util.HashMap;

public class Jianzhi61 {
    public boolean isStraight(int[] nums) {
        // 寻找最小的非零数和最大的非零数
        // 得到非零数的总个数和0的总个数
        // 最大和最小非零值之间有多少数字, 减去非零数字总个书再加上2, 得到还差几个数
        // 如果还差几个数等于0的个数, 那么你就true; 否则false;
        HashMap<Integer, Boolean> exists = new HashMap<>();
        int numZero = 0, numPositive = 0, maxPositive = 0, minPositive = Integer.MAX_VALUE;
        for (int num : nums){
            if (num == 0){
                numZero += 1;
            }
            else if (num > 0) {
                // 如果有重复的非0数字, 直接GG了嘛.
                if (exists.containsKey(num)) return false;
                exists.put(num, true);
                numPositive += 1;
                maxPositive = Math.max(num, maxPositive);
                minPositive = Math.min(num, minPositive);
            }
        }
        int howManyNumbersInBetween = maxPositive - minPositive - 1;
        int howManyZerosAreNeeded = howManyNumbersInBetween - numPositive + 2;
        // 只要后备的0的个数多于所需, 便返回true
        return howManyZerosAreNeeded <= numZero;
    }
    public static void main(String []args){
        Jianzhi61 s = new Jianzhi61();
        int [] nums = new int[]{0, 0, 1, 2, 5};
        System.out.print(s.isStraight(nums));
    }
}
