'''
[剑指 Offer 65. 不用加减乘除做加法 - 力扣（LeetCode）](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof)

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2

 

提示：


	a, b 均可能是负数或 0
	结果不会溢出 32 位整数

'''

class Solution:
    def add(self, a: int, b: int) -> int:
        # 32位数掩码
        mask = 0XFFFFFFFF
        # 32位数的最大正数
        posMx = 0X7FFFFFFF
        while b != 0:
            # a是不带进位的和, 都要转成32位整数
            # b是进位, 都要转成32位整数
            # 循环直到进位为0, 那么a就是最终结果
            smwithoutcarry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = smwithoutcarry, carry
        # 最终如果是32位负数的话, 需要将其转回python正常的负数表示形式(高于32位的全是1, 而不是32位负数那样更高位全为0), 做法是先对低 32 位的取反, 更高位不变, 然后整体再取反, 从而将大于等于 32 位的数字重新转成 1
        return a if a <= posMx else ~(a ^ mask)

### https://blog.csdn.net/zjulyx1993/article/details/108245454

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()