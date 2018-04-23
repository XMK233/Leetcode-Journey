/*
网上的方法比较同一，就是先对每一个字符串进行排序，
然后将排序了的字符串作为key，字符串的list作为value来设计hash表。
利用这个hash表，我们能够仅遍历原数组一次而将所有的字符串都找到归属。
时间复杂度就是O(nlogn)O(n)酱紫。
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        for (String str : strs){
            char []a = str.toCharArray();
            Arrays.sort(a);
            String tmpStr = new String(a);
            if (map.containsKey(tmpStr)){
                map.get(tmpStr).add(str);
            }
            else{
                map.put(tmpStr, new ArrayList<String>(Arrays.asList(str)));
            }
        }

        List<List<String>> res = new ArrayList<List<String>>();
        for (List<String> a : map.values()){
            res.add(a);
        }
        return res;
    }

    static public void main(String args[]){
        Solution s = new Solution();
        //String []a = {"eat", "tea", "tan", "ate", "nat", "bat"};
        String []a = {};
        System.out.println(s.groupAnagrams(a));
    }
}
