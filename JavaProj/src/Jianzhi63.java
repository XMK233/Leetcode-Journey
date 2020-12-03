public class Jianzhi63 {
    public int maxProfit(int[] prices) {
        // 其实思路是酱紫的：
        // 如果卖的话，就跟现在最低的价格比看能赚多少，要么不卖
        // 所以需要记录到目前为止的最低值
        int minVal = Integer.MAX_VALUE, maxEarn = 0;
        for (int price : prices) {
            minVal = Math.min(price, minVal);
            maxEarn = Math.max(price - minVal, maxEarn);
        }
        return maxEarn;
    }
    public static void main(String []args){
        Jianzhi63 s = new Jianzhi63();
        int [] nums = new int[]{7,6,4,3,1};
        System.out.print(s.maxProfit(nums));
    }
}
