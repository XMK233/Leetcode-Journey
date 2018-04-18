import java.util.*;
/*
如果用R语言实现jump1，那么再短的数组都会超时。不知为什么。
Jump1方法其实是一个动态规划，复杂度是n方，如果nums长的话就炸了。
网上抄的方法其实比较朴素。说破了就是：看看本次跳跃，能到一个什么区间。
这个区间有左右边界。
那么下一次跳跃的区间就是上一次跳跃的右边界的后一个直到从上一个区间开始能跳到的最远的地方。
总之就是尽量跳得更远，直到最后一个点处在某一次跳跃能达到得左右区间之内。
 https://blog.csdn.net/u011954296/article/details/51746150
* */
class Solution {
    public int jump1(int[] nums) {
        int size = nums.length;
        if (size == 0 || size == 1) return 0;

        int [][]dp = new int[size][size];
        for (int i = 0; i < size; i++){
            dp[i][i] = 0;
            for (int j = i + 1; j < size; j++){
                if ((j - i) == 1){
                    dp[i][j] = 1;
                }else{
                    dp[i][j] = -1;
                }
            }
        }

        for (int i = size - 1; i >= 0; i--){
            for (int j = i + 1; j < size; j++){

                if (dp[i][j] != -1)
                    continue;

                if (nums[i] >= (j - i)){
                    dp[i][j] = 1;
                }else{
                    int smallest = Integer.MAX_VALUE;
                    for (int k = i + 1; k < j; k++){
                        if ((dp[i][k] + dp[k][j]) < smallest){
                            smallest = dp[i][k] + dp[k][j];
                        }
                    }
                    dp[i][j] = smallest;
                }
            }
        }
        return dp[0][size - 1];
    }
    public int jump(int[] nums) {
        int l = 0;
        int r = 0;
        int next_r = 0;
        //k记录跳转到r需要的最少的次数
        int k = 0;
        while (r<nums.length - 1)
        {
            for (int i=l;i<=r;++i)
            {
                next_r = Integer.max(next_r, i+nums[i]);
            }
            //更新k次跳转能到达的左右两边下标的范围
            l = r+1;
            r = next_r;
            ++k;
        }
        return k;
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int []a = {1, 2, 1, 1, 1};
        System.out.print(s.jump(a));
    }
}
