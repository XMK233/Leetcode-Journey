import java.util.HashMap;

public class Jianzhi50 {
    public char firstUniqChar(String s) {
        HashMap<Character, Integer> letterNum = new HashMap<>();
        char [] chrs = s.toCharArray();
        // 用hash统计每一个字符出现的次数
        for (char chr : chrs){
            if (letterNum.containsKey(chr))
                letterNum.put(chr, letterNum.get(chr) + 1);
            else
                letterNum.put(chr, 1);
        }
        // 然后再遍历一遍原来的字符串, 找第一个只出现一次的数字.
        for (char chr : chrs){
            if (letterNum.get(chr) == 1)
                return chr;
        }

        return ' ';
    }
    public static void main(String []args){
        Jianzhi50 s = new Jianzhi50();
        int [] res = new int[]{7, 5, 6, 4};
        String s_ = "abaccdeff";
        System.out.print(s.firstUniqChar(""));
    }
}
