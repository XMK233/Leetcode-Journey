public class Jianzhi58I {
    public String reverseWords(String s){
        String [] strs = s.trim().split(" ");
        StringBuilder res = new StringBuilder();
        for (int i = strs.length - 1; i >= 0; i--){
            if (strs[i].equals("")) continue;
            res.append(strs[i] + " ");
        }
        return res.toString().trim();
//        https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/solution/mian-shi-ti-58-i-fan-zhuan-dan-ci-shun-xu-shuang-z/
    }
}
