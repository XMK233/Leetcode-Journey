'''中等
相关标签
premium lock icon
相关企业
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 

示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"
 

提示：

1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 将字符串按 Z 字形排列并逐行读出
        # 边界：只有一行或行数不小于字符串长度，直接返回原串
        if numRows == 1 or numRows >= len(s):
            return s
        # 每一行的字符累积容器
        rows = [''] * numRows
        # 当前所在行索引与行移动方向（step 为 +1 向下，-1 向上）
        i = 0
        step = 1
        for ch in s:
            # 把当前字符放入对应行
            rows[i] += ch
            # 首行/末行需要改变行移动方向
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            # 移动到下一行
            i += step
        # 拼接所有行得到最终结果
        return ''.join(rows)

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
        ("AB", 2, "AB"),
        ("ABC", 2, "ACB"),
    ]
    for s, r, expect in cases:
        out = sol.convert(s, r)
        print(f"s={s}, numRows={r} -> {out}")
        assert out == expect
    print("All tests passed")
