'''
[剑指 Offer 43. 1～n 整数中 1 出现的次数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof)

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

示例 1：

输入：n = 12
输出：5


示例 2：

输入：n = 13
输出：6

 

限制：


	1 <= n < 2^31


注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/
'''

'''
## https://leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode/
## 没看懂。
这题难度毕竟是困难的, 而且方法晦涩难懂. 还是算了罢. 估计不会考, 考了咱们也不会啊. 
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        countr = 0
        i = 1
        while i <= n:
            divider = i * 10
            countr += (n//divider) * i + min(max(n%divider - i + 1, 0), i)
            i *= 10
        return countr

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