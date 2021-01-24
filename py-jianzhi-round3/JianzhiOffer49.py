'''
[剑指 Offer 49. 丑数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/chou-shu-lcof)

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  


	1 是丑数。
	n 不超过1690。


注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
'''

'''
一定要记住一点. 新的丑数只能由老的丑数相乘得到. 基于这一点出发, 你才能进入后续的分析. 

## https://blog.csdn.net/mabozi08/article/details/88938205
## 丑数. 算法其实还算是很简单的.
## index2, index3, index5指的是, UglyList的这个位置上的数字应该乘以2, 3, 5.
## 然后, 把三个index指的数字分别乘以相应的2/3/5, 得到三个积, 从这三个积中得到最小的数字, 就是当前最新的丑数, 加入到UglyList列表中.
## 然后, 最新的丑数是通过哪个index得到的, 这个index就自增1. 同时, 如果最新的丑数还是另外两个数中某一个或两个的倍数, 那么对应的index也要自增1.
## 就是这么骚. 其实大概的流程, 自己试着跑一下, 能出来的, 也很容易理解.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        UglyList = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(n-1):
            newUgly = min(UglyList[index2]*2, UglyList[index3]*3, UglyList[index5]*5)
            UglyList.append(newUgly)
            if newUgly%2==0:
                index2+=1
            if newUgly%3 == 0:
                index3+=1
            if newUgly%5 == 0:
                index5+=1
        return UglyList[-1]

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