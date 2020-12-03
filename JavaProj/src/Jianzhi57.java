public class Jianzhi57 {
    public int[] twoSum(int[] nums, int target) {
        int [] res = new int[2];
        // 首尾两个位置. 如果和太大, 前指针右移; 如果和太小, 后指针右移.
        for (int headIndex = 0, tailIndex = nums.length - 1; headIndex < tailIndex; ){
            int sum = nums[headIndex] + nums[tailIndex];
            if (sum < target){
                headIndex++;
            }
            else if (sum > target){
                tailIndex--;
            }
            else{
                res[0] = nums[headIndex];
                res[1] = nums[tailIndex];
//                System.out.println(res[0]);
//                System.out.println(res[1]);
                break;
            }
        }
        return res;
    }
    public static void main(String []args){
        Jianzhi57 s = new Jianzhi57();
        int [] res = new int[]{10,26,30,31,47,60};
        s.twoSum(res, 40);
    }
}
