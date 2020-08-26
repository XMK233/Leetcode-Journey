class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # print(s)
        # print(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # print(dp)
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
                    # print(dp)
        return dp.pop()

## https://blog.csdn.net/fuxuemingzhu/article/details/79368360
## 自己也想了一下, 跟上面方法介绍的有点接近, 但是临门一脚踢不进啊. 遗恨失破题.

s = Solution()
print(s.wordBreak("applepenapple", ["leet", "code"]))

class Solution1:
    def wordBreak(self, s: str, wordDict) -> bool:
        ## 初始化一个列表
        record = [True]
        record += [False] * len(s)
        for word in wordDict:
            lenOfWord = len(word)
            for i in range(lenOfWord - 1, len(s)):
                piece = s[i - lenOfWord + 1 : i+1]
                ### 如果这一截跟word一样并且当前凑不出来, 才有处理的必要.
                if piece == word and record[i+1] == False:
                    ### 如果之前就是true, 那就可以凑的出来, 否则凑不出来.
                    if record[i - lenOfWord + 1] == True:
                        record[i+1] = True

        return record[-1]