public class Jianzhi64 {
    public int sumNums(int n) {
        if (n == 1) return 1;
        return n + sumNums(n - 1);

    }
    public static void main(String []args){
        Jianzhi64 s = new Jianzhi64();
        System.out.print(s.sumNums(9));
    }
}
