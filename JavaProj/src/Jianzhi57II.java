import java.util.ArrayList;

public class Jianzhi57II {
    // 这个方法利用的是两个指针.
    public int [][] findContinuousSequence(int target) {
        ArrayList<int []> res = new ArrayList<>();
        for (int head = 1, tail = 2; tail < target && head < tail; ){
            int sum = (head + tail) * (tail - head + 1) / 2;
            // 小于目标值, 右指针右移.
            if (sum < target){
                tail += 1;
            }
            // 大于目标值, 左指针右移.
            else if (sum > target){
                head += 1;
            }
            // 等于目标值, 那就保存当前的结果, 然后左指针右移一位, 开启新篇章.
            else{
                int [] tmp = new int[tail - head + 1];
                for (int i = 0; i < tail - head + 1; i++){
                    tmp[i] = head + i;
//                    System.out.print(tmp[i]);
                }
//                System.out.println();
                head++;
                res.add(tmp);
            }
        }
        int [][] resRtn = new int[res.size()][];
        for (int i = 0; i < res.size(); i++){
            resRtn[i] = res.get(i);
        }
        return resRtn;
    }
    // 其实还可以有一种方法. 就是设等差数列的项数是n, 起始值是x.
    // 然后利用等差数列求和公式, 得到目标值target.
    // 然后用这个公式反推x: x = t/n + (1-n)/2
    // 然后遍历所有可能的n, 如果能够解的整数x, 那么这个n和x就可以用来求出一个符合要求的等差数列.
    public static void main(String []args){
        Jianzhi57II s = new Jianzhi57II();
        s.findContinuousSequence(15);
    }
}
