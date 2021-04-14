# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/11ae12e8c6fe48f883cad618c2e81475?tpId=117&&tqId=37842&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。
（字符串长度不大于100000，保证字符串仅由'0'~'9'这10种字符组成）
示例1
输入
复制
"1","99"
返回值
复制
"100"
说明
1+99=100

可以取巧的. 因为python 自动帮我们处理了大数的问题. 所以不用担心.
'''

class Solution:
    def solve_1(self , s , t ):
        # write code here
        return str(int(s) + int(t))

    def solve(self, s, t):
        # 考前救急，野生代码拷过来的 背下来
        mlen = max(len(s), len(t))  # 取两者长度的最大值
        # 在两个数字字符串的前面补0 比如'1'.zfill(3)='001'
        s = s.zfill(mlen)
        t = t.zfill(mlen)
        carry = 0
        res = ''
        for i in range(-1, -mlen - 1, -1):  # 两个新的字符串 都是从后往前遍历 从前往后依次是个位到最高位的计算结果，所以结果也应该是反向输出
            last = int(s[i]) + int(t[i]) + carry
            if last > 9:
                carry = 1
                res += str(last - 10)
            else:
                carry = 0
                res += str(last)
        if carry:
            res += str(carry)
        return res[::-1]  # 最后将res反过来输出

print(
    Solution().solve("123456", "3452340527034570298354")
)