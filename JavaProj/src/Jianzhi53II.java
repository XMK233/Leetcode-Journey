public class Jianzhi53II {
    public int missingNumber(int[] nums) {
        //数组理论长度
        int n = nums.length + 1;
        // 假设不缺数字的话, 应该得到的和
        int theoreticalSum = (n*n - n)/2;
        // 实际上得到的和
        int actualSum = 0;
        for (int num : nums){
            actualSum += num;
        }
        //就看实际和和理论和的差距有多少
        return theoreticalSum - actualSum;
    }

    public static void main(String []args){
        Jianzhi53II s = new Jianzhi53II();
        int [] res = new int[]{1,2,3,4,5,6,7,8,9};
        System.out.print(s.missingNumber(res));
    }
}
