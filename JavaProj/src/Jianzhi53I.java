import java.util.HashMap;

public class Jianzhi53I {
    public int search(int[] nums, int target) {
        // 搜索右边界 right
        int i = 0, j = nums.length - 1;
        while(i <= j) {
            int m = (i + j) / 2;
            if(nums[m] <= target) i = m + 1;
            else j = m - 1;
        }
        int right = i;
        // 若数组中无 target ，则提前返回
        if(j >= 0 && nums[j] != target) return 0;
        // 搜索左边界 right
        i = 0; j = nums.length - 1;
        while(i <= j) {
            int m = (i + j) / 2;
            if(nums[m] < target) i = m + 1;
            else j = m - 1;
        }
        int left = j;
        return right - left - 1;
    }
//    作者：jyd
//    链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/
//    来源：力扣（LeetCode）
//    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    public int search1(int[] nums, int target) {
        // 直接hash
        HashMap<Integer, Integer> record = new HashMap<>();
        for (int num : nums){
            if (record.containsKey(num))
                record.put(num, record.get(num) + 1);
            else
                record.put(num, 1);
        }
        if (!record.containsKey(target)) return 0;
        return record.get(target);
    }
    public static void main(String []args){
        Jianzhi53I s = new Jianzhi53I();
        int [] res = new int[]{5,7,7,8,8,10};
        System.out.print(s.search(res, 8));
    }
}
