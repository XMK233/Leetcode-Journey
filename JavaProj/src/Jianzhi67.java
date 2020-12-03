public class Jianzhi67 {
    public int strToInt(String str) {
        char [] c = str.trim().toCharArray();
        if (c.length <= 0) return 0;
        //判断首字符, 正负号, 普通数字, 非数字直接GG.
        // 总体思路: 判断首字符为正负号或普通数字, 然后判断后续字符是否为数字, 若非则中断遍历, 返回, 即可.

        //startPoint意为, 自此位起遍历.
        // 并非固自首字符起遍历. 因首字符或为符号位, 故可跳过.
        int sign = 1, startPoint = 0;
        if (c[0] == '+'){
            startPoint = 1;
        }
        else if (c[0] == '-'){
            sign = -1;
            startPoint = 1;
        }
        // 此段乃本算法核心, 参考他人解法.
        // 其判断是否超限之法颇妙. 宜从之.
        int res = 0, boundary = Integer.MAX_VALUE / 10;
        for (int i = startPoint; i < c.length; i++){
            if (c[i] >= '0' && c[i] <= '9'){
                // 因Java有最大最小INT之虞, 故诸多判断异也.
                // 若以py实现之, 则无此虞. 盖py并无数字之上下限.
                if (res > boundary || res == boundary && c[i] > '7'){ // 这里, 如果c[i] <= 7, 那么就将这种情况当作普通情况处理. 只有大于7的情况会作为特殊情况处理.
                    // 此间if判断之法, 颇妙, 可学.
                    // 预先算好boundary, 实为间接使用min_val/max_val, 智也.
                    return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                }
                res = res * 10 + (c[i] - '0');
            }
            else{
                break;
            }
        }
        return sign * res;
        //https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/solution/mian-shi-ti-67-ba-zi-fu-chuan-zhuan-huan-cheng-z-4/
    }
    public static void main(String []args){
        Jianzhi67 s = new Jianzhi67();
        System.out.print(s.strToInt("2147483646"));
    }
}
