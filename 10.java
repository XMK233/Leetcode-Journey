/*
原本的思路是直接用循环遍历就行了，但是这样是有问题的。后来直接放弃了努力，直接网上找了一个方法抄了 。
https://www.jianshu.com/p/85f3e5a9fcda 

网上的思路呢，跟我不一样的地方在于，判断s是不是空串，是空串了又怎样；
然后主要研究p串是不是能够适配s串当前字符，如果适配又怎样递归，不适配又怎么样递归。
总之就是递归一定要用的。我原先的方法因为不用递归，所以没法处理一些复杂情况。
*/

class Solution {
    public boolean isMatch(String s, String p) {
        //这个方法是抄的，来源： https://www.jianshu.com/p/85f3e5a9fcda 
        if (p.isEmpty()) {
            return s.isEmpty();
        }
        
        if (p.length() == 1 || p.charAt(1) != '*') {
            if (s.isEmpty() || (p.charAt(0) != '.' && p.charAt(0) != s.charAt(0))) {
                return false;
            } else {
                return isMatch(s.substring(1), p.substring(1));
            }
        }
        
        while (!s.isEmpty() && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.')) {
            if (isMatch(s, p.substring(2))) {
                return true;
            }
            s = s.substring(1);
        }
        
        return isMatch(s, p.substring(2));
    }
    
    public boolean isMatch1(String s, String p) {
        //如果s和p直接就是相等的，那就直接返回true就好了
        //如果是.*直接返回true就好了。可以不用单独判断。
        //如果只有p = "*", 直接false。可以不用单独判断。
        //遍历两个字符串。
        //如果当前字符不符，那就判断：
            //p下一个是不是*号，若否，就返回false。若是，那就

        //优先判断万能正则表达式：[.\*]*
        int k = 0;
        for (; k < p.length(); k++){
            if (k % 2 == 1 && p.charAt(k) == '*') ;
            else if (k % 2 == 0) ;
            else break;
        }
        if (p.length() % 2 == 0 && k == p.length()) return true;


        int i = 0, j = 0;
        for (;i < s.length() && j < p.length(); i++, j++){
            if (s.charAt(i) == p.charAt(j)) continue;
            else {
                if (p.charAt(j) == '.'){
                    continue;
                }
                else if (p.charAt(j) == '*'){
                    if (j == 0) return false;
                    else{
                        if (p.charAt(j - 1) == '.') return true;
                        else{
                            for (;i < p.length() && s.charAt(i) == p.charAt(j - 1); i++){;}
                            i--;
                        }
                    }
                }
                else {
                    if (j == p.length()) return false;
                    else{
                        if (p.charAt(j + 1) == '*') {j++;i--;}
                        else return false;
                    }
                }
            }
        }
        if (i == s.length() && j == p.length()) return true;
        return false;
    }
}