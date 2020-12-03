public class Jianzhi56II {
    public int singleNumber(int[] nums) {
        // 位运算.
        // 遍历32位里面的每一位.
        // 在第i位, nums里面所有数字在这个位上是1的数字的个数, 看该数能被3整除.
        // 如果某一个位上1的个数不能被3整除, 那么所求的数在这个位上是1, 也就是因为它有个1, 导致的不能被3整除;
        int res = 0;
        for (int i = 1, mask = 1; i <= 32; i++, mask <<= 1){
            int cnt = 0;
            for (int num : nums){
                if ((num & mask) != 0){
                    cnt++;
                }
            }
            if (cnt % 3 != 0){
                res |= mask;
            }
        }
        return res;
    }
    public static void main(String []args){
        Jianzhi56II s = new Jianzhi56II();
        int [] res = new int[]{3,4,3,3};
        System.out.print(s.singleNumber(res));
    }
}
