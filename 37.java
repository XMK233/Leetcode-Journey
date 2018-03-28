import java.util.*;
/*
创建一个solvable辅助方法：
对每一个空格进行遍历。
如果这是个空格，我们就判断，如果填入每一个数字，这个空格所在行列块是不是合法的，同时填入这个数字后剩下的棋盘是solvable的（这里是递归），那么就返回true就好了；
否则就将这个格子还原成空格，填入下一个数字再做判断。
如果发现这个空格无论填1-9中的哪一个数字都不能解，那就返回false。

值得注意，这里判断所在行列块是不是合法的方法，可以用36题的方法替代。
但是36题的方法太过复杂，在这题里面，只要判断某个空格所在的那一行那一列和那一块是否是合法的就行了。
*/
class Solution {
    public void solveSudoku(char[][] board) {
        solvable(board);
    }

    public boolean solvable(char[][] board){
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                if (board[i][j] == '.'){
                    for (char k = '1'; k <= '9'; k++){
                        board[i][j] = k;
                        if (isValid(board, i, j) && solvable(board))
                            return true;
                        board[i][j] = '.';
                    }
                    return false;
                }
            }
        }
        return true;
    }

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

    private boolean isValid(char[][] board,int row,int col){
        for(int i = 0;i<9;i++){
            if(i!=col && board[row][i] == board[row][col])
                return false;
        }
        for(int i = 0;i<9;i++){
            if(i!=row && board[i][col] == board[row][col])
                return false;
        }
        int beginRow = 3*(row/3);
        int beginCol = 3*(col/3);
        for(int i = beginRow;i<beginRow+3;i++){
            for(int j = beginCol;j<beginCol+3;j++){
                if(i!=row && j!=col && board[i][j] == board[row][col])
                    return false;
            }
        }
        return true;
    }
}

public class helloworld {
    public static void main(String[] args){
        Solution s = new Solution();
        int a[] = {1, 3, 5, 6};
        char [][] b = { {'5','3','.','.','7','.','.','.','.'},
                        {'6','.','.','1','9','5','.','.','.'},
                        {'.','9','8','.','.','.','.','6','.'},
                        {'8','.','.','.','6','.','.','.','3'},
                        {'4','.','.','8','.','3','.','.','1'},
                        {'7','.','.','.','2','.','.','.','6'},
                        {'.','6','.','.','.','.','2','8','.'},
                        {'.','.','.','4','1','9','.','.','5'},
                        {'.','.','.','.','8','.','.','7','9'}};
        String w[] = {"word", "good", "best", "good"};
        //System.out.println(s.solveSudoku(b));
        s.solveSudoku(b);
        System.out.print(s.isValidSudoku1(b));
    }
}
