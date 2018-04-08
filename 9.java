/*
借用了第七题，直接调转过来之后判断是否相同就行了。注意我们没必要判断溢出，直接把溢出判断去掉就行了。
*/

class Solution {
    public int reverse(int x) {
        int xx = x;
        int newInt = 0, temp = 0;
        while(xx != 0){
            temp = newInt * 10 + xx % 10;
            /*if (temp / 10 != newInt)  //如果不等的话说明temp已经溢出了
                return 0;*/
            newInt = temp;
            xx /= 10;
        }
        //newInt = (newInt * 10 + currentHigh);
        return newInt;
    }
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int xx = reverse(x);
        if (xx == x) return true;

        return false;
    }
}