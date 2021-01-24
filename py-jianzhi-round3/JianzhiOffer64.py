'''
[剑指 Offer 64. 求1+2+…+n - 力扣（LeetCode）](https://leetcode-cn.com/problems/qiu-12n-lcof)

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6


示例 2：

输入: n = 9
输出: 45


 

限制：


	1 <= n <= 10000

'''

class Solution:
    def sumNums(self, n: int) -> int:
        """
        python中的与（and）、或（or）、非（not）与java和c的不同之处在于
        A and B: 若A为False或其他空值（如：0, [], {}, ""等），则短路（不用再判断B是否为真，整个逻辑表达式已经为False了）
	    A or B: 如果A已经不是false了, 那就直接返回B, 无论B是什么东西, 哪怕是一个字符串, 也会原样返回.
        """
        return n and (n + self.sumNums(n-1))

## https://blog.csdn.net/besmarterbestronger/article/details/106480726
## 不用乘除，条件运算符之类的东西，那么就可以考虑利用递归来做了。
## 至于最后的返回类型，更是利用了python里面的技巧。
## 什么呢？
### 如果and的左边是1，那么返回and右边的值，而不一定是返回bool值。
### 如果or左边是0，那么直接返回or右边的值，而不一定是bool值。

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