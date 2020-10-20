public class jianzhi10II {
    public int numWays(int n) {
        int a = 1, b = 1, sum;
        for(int i = 0; i < n; i++){
            sum = (a + b) % 1000000007;
            a = b;
            b = sum;
        }
        return a;
    }
    public static void main(String []args){
        jianzhi10II s = new jianzhi10II();
        System.out.println(s.numWays(0));
    }
}
/*本质上, 这道题跟前一题没什么差别. */
