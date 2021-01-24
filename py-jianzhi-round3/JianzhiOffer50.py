'''
[剑指 Offer 50. 第一个只出现一次的字符 - 力扣（LeetCode）](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof)

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "


 

限制：

0 <= s 的长度 <= 50000
'''
'''
## https://blog.csdn.net/mabozi08/article/details/8893845
## 暴力解法. 没什么花架子.
'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        # write code here
        if not s:
            return " "
        tableSize = 256
        hashTable = [0]*tableSize
        for i in range(len(s)):
            hashTable[ord(s[i])]+=1
        for i in range(len(s)):
            if hashTable[ord(s[i])]==1:
                return s[i]
        return " "
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