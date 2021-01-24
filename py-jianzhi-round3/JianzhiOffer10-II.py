'''
[剑指 Offer 10- II. 青蛙跳台阶问题 - 力扣（LeetCode）](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof)

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2


示例 2：

输入：n = 7
输出：21


示例 3：

输入：n = 0
输出：1

提示：


	0 <= n <= 100


注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/

 
'''
'''
这个题, 最本质的解法应该是酱紫的: f(n) = f(n - 1) + f(n - 2). 
然后你一看这个, 哟呵, 不就是斐波那契数列嘛. 
所以直接用斐波那契数列的思路就可以解了. 

但有一个区别点: 之前那道题, a开始的时候是0, 现在是1. 
'''
class Solution:
    def numWays(self, n: int) -> int:
        ## 这道题跟普通的斐波那契数列是不一样的.
        a = 1
        b = 1
        for i in range(n):
            tmp = (a + b) % 1000000007
            a = b
            b = tmp
        return a


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