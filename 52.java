/*
参考了上一道题的方法，一点点改进罢了。
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
    public int process(int []record, int i, int n){
        if (i == n){
            return 1;
        }//说明可以放置n个皇后。

        int res = 0;
        for (int j = 0; j < n; j++){
            if (isValid(record, i, j)){
                record[i] = j;
                res += process(record, i + 1, n);
            }
        }
        return res;
        //还要判断是否能把剩下的皇后放进去。
    }

    public boolean isValid(int []record, int i, int j){
        for (int k = 0; k < i; k++){
            if ((record[k] == j) || (Math.abs(record[k] - j) == Math.abs(k - i)) )
                return false;
        }
        return true;
    }
    public int totalNQueens(int n) {
        int [] record = new int[n];
        return this.process(record, 0, n);
    }

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<List<String>>();
        int [] record = new int[n];
        this.process(record, 0, n);
        return res;
    }

    static public void main(String args[]){
        Solution s = new Solution();
        //String []a = {"eat", "tea", "tan", "ate", "nat", "bat"};
        String []a = {};
        System.out.println(s.totalNQueens(4));
    }
}
