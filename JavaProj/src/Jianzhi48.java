import com.sun.org.apache.xml.internal.dtm.ref.DTMAxisIterNodeList;

import java.util.HashMap;

public class Jianzhi48 {
    public int lengthOfLongestSubstring(String s) {
        // 记录每一个字符第一次出现的位置. positionOfChar
        // 还要记录当前最长字符串的头的位置. head.
        // 如果发现了字符重复了, 并且重复的字符都在head的后面, 那么最长的非重复串须得从重复的字符串后面一个字符开始. 更新head和positionsOfChar.
        // 随时记录最长的长度.
        HashMap<Character, Integer> positionOfChar = new HashMap<>();
        int head = 0, maxLength = 0;
        char [] chrs = s.toCharArray();
        for (int i = 0; i < chrs.length; i++){
            char chr = chrs[i];
            //
            if (!positionOfChar.containsKey(chr)){
                positionOfChar.put(chr, i);
            }
            // 若非第一次碰上, 就要进一步判断了.
            else{
                int lastPosition = positionOfChar.get(chr);
                // 如果重复的地方在head后面, head就要移动了.
                if (lastPosition >= head)
                    head = lastPosition + 1;
                // 更新长度和chr出现的位置.
                positionOfChar.put(chr, i);
            }
            // 无论有没有碰上重复的, 都要更新长度, 虽然不见得会有确实的变化.
            int newLength = i - head + 1;
            maxLength = Math.max(maxLength, newLength);
        }
        return maxLength;
    }
    public static void main(String []args){
        Jianzhi48 s = new Jianzhi48();
        int [] res = new int[]{7, 5, 6, 4};
        String s_ = "abaccdeff";
        System.out.print(s.lengthOfLongestSubstring(""));
    }
}
