class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        many_s = str.split()
        if len(pattern) != len(many_s):
            print(len(pattern), len(many_s))
            return False
        c_s = {}
        s_c = {}
        for c, s in zip(pattern, str.split()):
            print(c, s)
            if c not in c_s and s not in s_c:
                c_s[c] = s
                s_c[s] = c
            elif c in c_s and s in s_c:
                if (c == s_c[s] and s == c_s[c]):
                    pass
                else:
                    return False
            else:
                return False
        return True


s = Solution()
print(s.wordPattern("abba", "cat gog gog cat"))
