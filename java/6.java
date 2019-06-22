/*
Java实现的。
复习了java的基本语法，知道了：vector大概怎么用；stringbuilder怎么用；字符串末尾没有\0.

*/

class Solution {
    public String convert(String s, int numRows){
        //Vector<Integer> v = new Vector<Integer>();
        int [] v = new int[s.length()];
        if (numRows == 1) return s;
        for (int i = 0, dir = 1, counter = 1; i < s.length(); i++){
            //v.add(counter);
            v[i] = counter;
            if (counter == 1) dir = 1;
            else if (counter == numRows) dir = -1;
            counter = dir > 0 ? counter + 1 : counter - 1;
        }

        StringBuilder newString = new StringBuilder("");
        for (int i = 1; i <= numRows; i++){
            for (int j = 0; j < v.length; j++){
                if (v[j] == i){
                    newString.append(s.charAt(j));
                }
            }
        }

        /*for (int i = 0; i < v.size(); i++){
            System.out.print(v.get(i));
        }
        System.out.print(newString);*/
        return newString.toString();
    }
}