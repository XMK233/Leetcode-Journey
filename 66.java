/* 66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
*
*
* Solutions:
* Nothing particular.
* Be careful that if the array is 9, 9, ....9, you should add a new digit 1 in front of the old array. 
*
* */
class Solution {
    public int[] plusOne(int[] digits) {
        int moreDigits = 0;

        if (digits[digits.length - 1] != 9){
            digits[digits.length - 1] += 1;
        }
        else{
            for (int i = digits.length - 1, e = 1; i >= 0; i--){
                if (e == 1){
                    if (digits[i] == 9){
                        digits[i] = 0;
                        if (i == 0){
                            moreDigits = 1;
                            break;
                        }
                    }
                    else{
                        digits[i] += 1;
                        e = 0;
                    }
                }
                else{
                    break;
                }
            }
            if (moreDigits == 1){
                int [] newArray= new int[digits.length + 1];
                newArray[0] = 1;
                return newArray;
            }
        }


        return digits;
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
        int a [] = {9, 9, 9};
        int b [] = s.plusOne(a);
        for (int i = 0; i <= b.length - 1; i++){
            System.out.print(b[i]);
        }
    }
}
