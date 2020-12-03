//import com.sun.org.apache.xpath.internal.operations.String;

public class Jianzhi58II {
    public String reverseLeftWords(String s, int n){
        StringBuilder res = new StringBuilder();
        for (int i = n; i < s.length(); i++){
            res.append(s.charAt(i));
        }
        for (int i = 0; i < n; i++){
            res.append(s.charAt(i));
        }
        return res.toString();
//        https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/mian-shi-ti-58-ii-zuo-xuan-zhuan-zi-fu-chuan-qie-p/
    }
}
