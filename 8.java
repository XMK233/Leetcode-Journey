/*
怎么把字符串转为ascii码，其实就是强制类型转换就好了。
Integer.MAX_VALUE和Integer.MIN_VALUE反映了integer的最大最小值。
根据题目的提示，我总结了如下要注意的情况：
起始空格、起始为正负号、过长的字符串（可以借鉴上一题的溢出判断）、第一个非空白字符非法、空串、全空白字符串等。
*/

class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        if (str.equals("")) return 0;

        int minusFlag = 1;
        int headShift = 0;
        if ((int)str.charAt(0)  > 57 || (int)str.charAt(0)  < 48) {
            if (str.charAt(0) == '+' || str.charAt(0) == '-'){
                minusFlag = str.charAt(0) == '+' ? 1 : -1;
                headShift = 1;
            }
            else
                return 0;
        }
        int newInt = 0;
        for (int i = headShift; i < str.length(); i++){
            if ((int)str.charAt(i)  <= 57 && (int)str.charAt(i)  >= 48){
                int temp = newInt * 10 + ((int)str.charAt(i) - 48);
                if (temp / 10 != newInt) return minusFlag == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                newInt = temp;
            }
            else {
                if (i == headShift){
                    return 0;
                }
                else
                    break;
            }
        }


        return newInt * minusFlag;
    }
}