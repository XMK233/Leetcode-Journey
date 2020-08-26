class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 如果字符串s的长度少于k，那么一定不存在满足题意的子字符串，返回0；
        if len(s) < k:
            return 0

        # 如果一个字符在s中出现的次数少于k次，那么所有的包含这个字符的子字符串都不能满足题意。所以，应该去不包含这个字符的子字符串继续寻找。这就是分而治之的思路，返回不同子串的长度最大值。
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))

        # 如果s中的每个字符出现的次数都大于k次，那么s就是我们要求的字符串。
        return len(s)

## https://blog.csdn.net/fuxuemingzhu/article/details/82889933