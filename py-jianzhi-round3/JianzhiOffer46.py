'''
[剑指 Offer 46. 把数字翻译成字符串 - 力扣（LeetCode）](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof)

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

 

提示：


	0 <= num < 231

'''
'''
## 然后呢, 遍历原字符串. 如果遍历到当前的i能和前面的那一个字符组合成0~25之间的数字, 那就有两种组合情况, 一种是这个i为单独的字符串, 一种是i和前面一个组合
### 成一个数字的情况. 两种情况能凑成的解法数量加起来就可以了.
### 注意, 这里有一个坑. 就是如果i前面那一个字符是0, 是不能看作"i和前面一个字符可以组合成一个数字"的哦.
## 然后, 如果i不能和前面一个字符组成合法数字, 那就只能把i当成一个单独的字符来翻译了. 
'''
class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        ##
        if len(s) == 1:
            return 1
        ##
        dp = [1] * (len(s) + 1)
        s = "x" + s

        for i in range(2, len(s)):
            sec = int(s[i - 1: i + 1])
            if s[i - 1] != "0" and sec >= 0 and sec <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]

s = Solution()
print(s.translateNum(506))

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