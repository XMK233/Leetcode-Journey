import java.util.ArrayList;

public class Jianzhi49 {
    public int nthUglyNumber(int n) {
        // 首先要解决, 怎么遍历所有的丑数?
        // 遍历的方法是:
        // 设置三个数, indexOf2, indexOf3, indexOf5, 表示多少个2/3/5相加.
        // 然后, 每一次都做uglyNums.get(indexOfX) * X, 得到三个积, 取最小的那个作为下一个丑数.
        // 然后, indexOfX要递增, 表示下一次的积是要变大的了.
        // 注意这样一个情况: uglyNums.get(indexOf2) = 3, uglyNums.get(indexOf3) = 2的时候, 他俩乘积一样, 那么他们的indexOf3要同时增大, 否则丑数6会出现两次.
        ArrayList<Integer> uglyNums = new ArrayList<>();
        uglyNums.add(1);
        int indexOf2 = 0, indexOf3 = 0, indexOf5 = 0;
        int currentUglyNum = -1;
        while (uglyNums.size() < n){
            currentUglyNum = Math.min(Math.min(uglyNums.get(indexOf2) * 2, uglyNums.get(indexOf3) * 3), uglyNums.get(indexOf5) * 5);
            uglyNums.add(currentUglyNum);
            if (currentUglyNum % 2 == 0) indexOf2++;
            if (currentUglyNum % 3 == 0) indexOf3++;
            if (currentUglyNum % 5 == 0) indexOf5++;
        }
        return uglyNums.get(uglyNums.size() - 1);
    }
    public static void main(String []args){
        Jianzhi49 s = new Jianzhi49();
        int [] res = new int[]{7, 5, 6, 4};
        String s_ = "abaccdeff";
        System.out.print(s.nthUglyNumber(11));
    }
}
