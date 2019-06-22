'''
    5. Longest Palindromic Substring   
python。
关键点：一个是动态规划，一个是dp[i][i - 1]这一部不要漏掉，有了这个才能判断两个连续的相同字符是回文。
我的实现方法是倒过来的，也就是从最后一行最后一列开始，先遍历列再遍历行，最后才到第一行第一列。 

'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        dp = [[False] * length for i in range(length)]

        longest = 1
        head = 0

        for ii in range(length):
            dp[ii][ii] = True
            if ii > 0:
                dp[ii][ii - 1] = True

        i = length - 1
        j = length - 1
        while i >= 0:
            while j >= 0:
                if i == j:
                    break
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1] == 1)
                    if dp[i][j] == True:
                        l = j - i + 1
                        if l > longest:
                            head = i
                            longest = l
                j -= 1
            j = length - 1
            i -= 1

        #print(s[head: head + longest])
        return s[head: head + longest]
        