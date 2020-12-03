public class Jianzhi65 {
    public int add(int a, int b) {
        // 位运算.
        // 亦即, 异或乃不进位加法, 与可得进位.
        int sumWithoutCarry = -1, carry = -1;
        // 辗转运算, 直至无进位乃止.
        while (b != 0){
            sumWithoutCarry = a ^ b;
            carry = a & b;
            a = sumWithoutCarry;
            b = carry << 1;
        }
        return a;
    }
    public static void main(String[]args){
        Jianzhi65 s = new Jianzhi65();
        System.out.println(s.add(12, 24));
    }
}
