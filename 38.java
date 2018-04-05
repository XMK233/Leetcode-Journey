import java.util.*;

class Solution {
    public String countAndSay(int n) {
        if (n == 1)
            return "1";

        String lastOne = countAndSay(n - 1);
        StringBuilder currOne = new StringBuilder("");


        char cur = lastOne.charAt(0);
        int count = 1;

        for (int i = 1; i < lastOne.length(); i++){
            if (lastOne.charAt(i) == cur)
                count++;
            else{
                currOne.append(String.valueOf(count));
                currOne.append(String.valueOf(cur));
                cur = lastOne.charAt(i);
                count = 1;
            }
        }

        currOne.append(String.valueOf(count));
        currOne.append(String.valueOf(cur));


        return currOne.toString();
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.print(s.countAndSay(5));
    }
}
