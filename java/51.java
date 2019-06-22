/*
参考了 https://blog.csdn.net/u013564276/article/details/51244581 的实现方法。
比较精妙的地方在于：利用了一个一维数组，记录某一行里面，皇后要放到哪一列中。然后逐行去讨论，每一个列是否应该放置一个，如果可以的话，就递归到下一行。
（判断某一个位置可以不可以放其实很容易实现，不表）
这里有一个问题一直没搞懂，就是queenList数组，或者说，记录棋盘放置情况的数组，为什么回溯了之后，不要把原来的记录删掉？
*/
class Solution {
    public void process(int []record, int i, int n, List<List<String>> res){
        if (i == n){
            List<String> tmp = new ArrayList<String>();
            for (int line = 0; line < n; line++){
                StringBuilder s = new StringBuilder();
                for (int l = 0; l < n; l++){
                    s.append(".");
                }
                s.replace(record[line], record[line] + 1, "Q");
                tmp.add(s.toString());
            }
            res.add(tmp);
        }//说明可以放置n个皇后。

        for (int j = 0; j < n; j++){
            if (isValid(record, i, j)){
                record[i] = j;
                process(record, i + 1, n, res);
            }
        }
        //还要判断是否能把剩下的皇后放进去。

    }

    public boolean isValid(int []record, int i, int j){
        for (int k = 0; k < i; k++){
            if ((record[k] == j) || (Math.abs(record[k] - j) == Math.abs(k - i)) )
                return false;
        }
        return true;
    }

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<List<String>>();
        int [] record = new int[n];
        this.process(record, 0, n, res);
        return res;
    }
}