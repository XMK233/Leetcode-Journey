import java.util.*;

class Solution{
    public int longestValidParentheses(String s) {
        Stack<Integer> status = new Stack<Integer>();
        int lgtLen = 0; //longest length
        //-1: (; -2: )
        for (int i = 0; i < s.length(); i++){
            //若是左括号
            if (s.charAt(i) == '(') status.push(-1);
                //若是右括号
            else {
                //是为空栈
                if (status.size() == 0) ;
                    //不是空栈
                else{
                    int top = status.pop();
                    //如果栈顶元素是左括号
                    if (top == -1) {status.push(2);
                        lgtLen = 2 > lgtLen ? 2 : lgtLen;}
                    //如果栈顶元素是数字
                    else {
                        int curLen = top;
                        while (status.size() != 0){
                            top = status.pop();
                            if (top == -1) {
                                status.push(curLen + 2);
                                lgtLen = curLen > lgtLen ? curLen : lgtLen;
                                break;
                            }
                            else curLen += top;
                        }
                        if (status.size() == 0){
                            lgtLen = curLen > lgtLen ? curLen : lgtLen;
                        }
                    }
                }
            }
        }

        for (int curLen = 0; status.size() != 0; ){
            int curItem = status.pop();
            if (curItem > 0) {
                curLen += curItem;
                lgtLen = curLen > lgtLen ? curLen : lgtLen;
            }
            else {curLen = 0;}
        }
        return lgtLen;
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int a[] = {5, 4, 7, 5, 3, 2};
        String w[] = {"word", "good", "best", "good"};
        //s.longestValidParentheses(")()())");
        System.out.println(s.longestValidParentheses(")()())()()("));//
    }
}
