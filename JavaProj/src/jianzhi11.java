public class jianzhi11 {
    public int minArray(int[] numbers) {
        int head = 0, tail = numbers.length - 1;
        while (head < tail) {
            if (numbers[head] < numbers[tail])
                return numbers[head];
            int mid = (tail - head) / 2 + head;
            if (/*numbers[mid] > numbers[head] &&*/ numbers[mid] > numbers[tail]) {
                head = mid + 1; //这里增加1
            } else if (/*numbers[mid] < numbers[head] &&*/ numbers[mid] < numbers[tail]) {
                tail = mid; //这里不要增加1.
            } else{
                tail--;//当 nums[m] = nums[j]nums[m]=nums[j] 时： 无法判断 mm 在哪个排序数组中，即无法判断旋转点 xx 在 [i, m][i,m] 还是 [m + 1, j][m+1,j] 区间中。解决方案： 执行 j = j - 1j=j−1 缩小判断范围
            }
        }
        return numbers[head];
    }
    public static void main(String[] args) {
        jianzhi11 s = new jianzhi11();
        System.out.println(s.minArray(new int[]{3, 4, 5, 1, 2}));
    }
}
/*没有完全弄出来.
mid, mid+1这两个地方参考了答案.
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
else里面也是参考了的. 这种情况就是numbers[mid] < numbers[tail], 没法判断, 那就把tail往回缩一格, 重新判断.
但是其他的地方基本是自己想出来并实现的. 并且程序的大致结构上已经和参考答案别无二致了.
*/