public class Jianzhi56I {
    public int[] singleNumbers(int[] nums) {
        // 位运算.

        // 将所有的数字异或起来, 得到的值肯定相当于两个单身狗的异或结果.
        int exclusiveOrRst = nums[0];
        for (int i = 1; i < nums.length; i++){
            exclusiveOrRst ^= nums[i];
        }
        // 然后随便找这个异或结果的一个为1的位.
        int mask = 1;
        for (int i = 1; i <= 32; i++, mask <<= 1){
            if ((exclusiveOrRst & mask) > 0)
                break;
        }
        // 按照这个位是0或是1将nums里面的数字分为两拨.
        // 然后两拨数字里面各自异或, 就能各自得到一个单身狗了.
        int exclusiveOrRst0 = -1, exclusiveOrRst1 = -1;
        for (int i = 0; i < nums.length; i++){
            //这里犯错了. 因为这里应该用&, 我原来是用了^, 所以错了.
            int tmpRst = nums[i] & mask;
            //
            if (tmpRst != 0){
                if (exclusiveOrRst1 < 0)
                    exclusiveOrRst1 = nums[i];
                else
                    exclusiveOrRst1 ^= nums[i];
            }
            else{
                if (exclusiveOrRst0 < 0)
                    exclusiveOrRst0 = nums[i];
                else
                    exclusiveOrRst0 ^= nums[i];
            }

        }
        int []res = new int[2];
        res[0] = exclusiveOrRst0;
        res[1] = exclusiveOrRst1;
//        System.out.println(res[0]);
//        System.out.println(res[1]);
        return res;
    }
    public static void main(String []args){
        Jianzhi56I s = new Jianzhi56I();
        int [] res = new int[]{1,2,10,4,1,4,3,3};
        s.singleNumbers(res);
    }
}
