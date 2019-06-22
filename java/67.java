/* 67 Add binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
*
*
* Solutions:
* nothing particular.
* make two array length the same.
* and then add them digit by digit.
* consider the moreDigit. 中文是进位。
*
* */
class Solution {
    public String addBinary(String a, String b) {
        String c = a.length() > b.length() ? a : b;
        String d = c == a ? b : a;
        //C is the longer one and the D is the shorter one,
        int moreDigits = 0;
        String ret = "";

        for (int i = 0, delta = c.length() - d.length( ); i < delta; i++){
            d = "0" + d;
        }

        for (int i = c.length() - 1; i >= 0; i--) {
            int fromC = c.charAt(i) - '0', fromD = d.charAt(i) - '0', more = moreDigits - 0;
            int sum = fromC + fromD + more;
            if (sum == 3){
                ret = "1" + ret;
                moreDigits = 1;
            }
            else if (sum == 2){
                ret = "0" + ret;
                moreDigits = 1;
            }
            else if (sum == 1){
                ret = "1" + ret;
                moreDigits = 0;
            }
            else {
                ret = "0" + ret;
                moreDigits = 0;
            }
        }
        if (moreDigits == 1){
            ret = "1" + ret;
        }
        return ret;
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        String a = "1010", b = "1011";
        System.out.print(s.addBinary(a, b));
    }
}
