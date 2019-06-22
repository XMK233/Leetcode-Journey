/*
* The problem:
 Given a string s consists of upper/lower-case alphabets and empty space characters ' ',

return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
*
* Solutions:
* Nothing particular.
*
* */
class Solution{
    public int lengthOfLastWord(String s) {
        String a [] = s.split(" ");
        if (a.length == 0){
            return 0;
        }
        return a[a.length - 1].length();
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        String a = " ";
        System.out.print(s.lengthOfLastWord(a));
    }
}