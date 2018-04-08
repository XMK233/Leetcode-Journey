/*
其实就是判断了。
用了一个二维数组来存个位、十位等位可能出现的字符，因为百位、十位、个位的计算方式完全一样，不同的就是不同的位应该用不同的字符集。

*/
class Solution {
    public String intToRoman(int num) {
        StringBuilder rom = new StringBuilder();
        char elements[][] = {{'I', 'V', 'X'}, {'X', 'L', 'C'}, {'C', 'D', 'M'}, {'M', '?', '?'}};
        int i = 0;
        while (num != 0){
            int last = num % 10;
            if (last >= 1 && last <= 3){
                for (int j = 0; j <last; j++) rom.append(elements[i][0]);
            }
            else if (last == 4){
                rom.append(elements[i][1]); rom.append(elements[i][0]);
            }
            else if (last == 5){
                rom.append(elements[i][1]);
            }
            else if (last >= 6 && last <= 8){
                for (int j = 0; j < last - 5; j++ ) rom.append(elements[i][0]);
                rom.append(elements[i][1]);
            }
            else if (last == 9){
                rom.append(elements[i][2]); rom.append(elements[i][0]);
            }
            num /= 10;
            i++;
        }
        return rom.reverse().toString();
    }
}