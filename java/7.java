/*
技巧其实就是一个，那就是判断什么时候溢出。
因为不知道leetcode后台到底整数的上下限是多少，所以我搜到一个技巧，就是按照原来的逻辑，
当前的值乘以10加上后一位数后，再除以10，如果跟当前值不一样了，就是溢出了，就可以直接返回0了。
*/

class Solution {
    public int reverse(int x) {
        int xx = x;
        int newInt = 0, temp = 0;
        while(xx != 0){
            temp = newInt * 10 + xx % 10;
            if (temp / 10 != newInt)  //如果不等的话说明temp已经溢出了
                return 0;
            newInt = temp;
            xx /= 10;
        }
        //newInt = (newInt * 10 + currentHigh);
        return newInt;
    }
}