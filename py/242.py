class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## 长度不一, 直接不要计算了.
        if len(s) != len(t):
            return False
        ## 长度一致, 用传说中的hash大法.
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
                if d[c] == 0:
                    d.pop(c)
        return True

s = Solution()
print(s.isAnagram("anagram", "nataram"))