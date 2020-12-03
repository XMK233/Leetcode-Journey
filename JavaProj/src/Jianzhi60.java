public class Jianzhi60 {
    public double[] dicesProbability(int n) {
        // 最核心的思路是, 先获得, 从点数n到6n, 每一种点数有多少种情况.
        // 然后, 每一个情况数乘上(1/6)**n, 得到的就是获得这一点数的概率.
        // 然则如何计算每一种点数有几多情况, 可用动归.
        // x为点数;
        // f(n, x) = f(n-1, x-1) + f(n-1, x-2) + ... f(n-1, x-6)

        // 初始化dp数组
        int [][] dp = new int[n][6*n];
        // 第一行, 就是1个骰子, 能投出来的点数
        for (int i = 0; i < 6; i++){
            dp[0][i] = 1;
        }
        // 然后后面的每一行:
        for (int row = 1; row < n; row++){
            for (int col = row; col < 6 * (row + 1); col++){
                int res = 0;
                for (int j = 1; j <= 6; j++){
                    if (col - j < 0) break;
                    res += dp[row - 1][col - j];
                }
                dp[row][col] = res;
            }
        }
        // 然后生成最后的结果列表
        double [] finRes = new double[6 * n - n + 1];
        double baseProbability = 1.0/Math.pow(6.0, n);
        for (int i = n - 1, j = 0; i < 6 * n; i++, j++){
            finRes[j] = dp[n-1][i] * baseProbability;
//            System.out.println(finRes[j]);
        }
        return finRes;
    }
    public static void main(String []args){
        Jianzhi60 s = new Jianzhi60();
        int [] nums = new int[]{0, 0, 1, 2, 5};
        System.out.print(s.dicesProbability(2));
    }
}
