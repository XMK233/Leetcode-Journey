public class Jianzhi62 {
    public int lastRemaining(int n, int m) {
        int ans = 0;
        // 最后一轮剩下2个人，所以从2开始反推
        for (int i = 2; i <= n; i++) {
            ans = (ans + m) % i;
        }
        return ans;
    }
//    作者：sweetieeyi
//    链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
//    来源：力扣（LeetCode）
//    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    public int lastRemaining1(int n, int m) {
        // 我认为这里如果要遍历的话, 还是应该用while. 因为数组的长度一直在缩短.
        // 主要是, 当前的index加上m之后求余, 得到新的index.
        // 然后从数组中删掉这个数字
        // 然后改变长度



        return 0;
    }

    public static void main(String []args){
        Jianzhi62 s = new Jianzhi62();
        System.out.print(s.lastRemaining(5, 3));
    }
}
