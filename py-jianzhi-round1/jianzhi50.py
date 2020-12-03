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

## https://blog.csdn.net/mabozi08/article/details/8893845
## 暴力解法. 没什么花架子.