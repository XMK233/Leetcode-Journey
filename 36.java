/*
首先，我们要判断的问题非常明了，就是判断已经存在了的数字，是否已经出现了重复（行重复，列重复，块重复）。
确定一个外层i循环，range 9；内层j循环，range也是9。然后呢，同时遍历行列块，利用hash手段来判断某个字符是否已经出现过了。
遍历块的方法稍显数学功力，关键点在于如何利用整除和取余手法来实现矩阵元素的遍历。这边就不再做介绍了，有心之人很快就会明白过来。
*/

import java.util.*;

class Solution {
    public boolean isValidSudoku1(char[][] board) {
        for(int i = 0; i<9; i++){
            HashSet<Character> rows = new HashSet<Character>();
            HashSet<Character> columns = new HashSet<Character>();
            HashSet<Character> cube = new HashSet<Character>();
            for (int j = 0; j < 9;j++){
                if(board[i][j]!='.' && !rows.add(board[i][j]))
                    return false;
                if(board[j][i]!='.' && !columns.add(board[j][i]))
                    return false;
                int RowIndex = 3*(i/3);
                int ColIndex = 3*(i%3);
                if(board[RowIndex + j/3][ColIndex + j%3]!='.' && !cube.add(board[RowIndex + j/3][ColIndex + j%3]))
                    return false;
            }
        }
        return true;

    }
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++){
            HashMap<Character, Integer> raw = new HashMap<>();
            HashMap<Character, Integer> col = new HashMap<>();
            HashMap<Character, Integer> cube = new HashMap<>();
            int cubeShiftX = i / 3 * 3, cubeShiftY = i % 3 * 3;
            for (int j = 0; j < 9; j++){
                if (board[i][j] != '.') {
                    if (raw.containsKey(board[i][j]))
                        return false;
                    else
                        raw.put(board[i][j], 1);
                }

                if (board[j][i] != '.') {
                    if (col.containsKey(board[j][i]))
                        return false;
                    else
                        col.put(board[j][i], 1);
                }

                if (board[cubeShiftX + j / 3][cubeShiftY + j % 3] != '.') {
                    if (cube.containsKey(board[cubeShiftX + j / 3][cubeShiftY + j % 3]))
                        return false;
                    else
                        cube.put(board[cubeShiftX + j / 3][cubeShiftY + j % 3], 1);
                }
            }
        }
        return true;
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int a[] = {1, 3, 5, 6};
        char [][] b = { {'.','.','.','.','.','.','.','.','.'},
                        {'.','.','.','.','.','.','3','.','.'},
                        {'.','.','.','1','8','.','.','.','.'},
                        {'.','.','.','7','.','.','.','.','.'},
                        {'.','.','.','.','1','.','9','7','.'},
                        {'.','.','.','.','.','.','.','.','.'},
                        {'.','.','.','3','6','.','1','.','.'},
                        {'.','.','.','.','.','.','.','.','.'},
                        {'.','.','.','.','.','.','.','2','.'}};
        String w[] = {"word", "good", "best", "good"};
        System.out.println(s.isValidSudoku(b));
    }
}
