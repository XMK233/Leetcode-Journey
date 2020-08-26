class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ## 不一样长, 还有什么好说的? 无非也是有缘无份罢了.
        if len(s) != len(t):
            return False
        ## 一样长的, 就骑驴看唱本——走着瞧.
        ls = []
        lt = []
        for cs, ct in zip(s, t):
            ## 东风不与周郎便，两者应当各自瞧。
            if cs not in ls:
                ls.append(cs)
            if ct not in lt:
                lt.append(ct)
            if not lt.index(ct) == ls.index(cs):
                return False
        return True


s = Solution()
print(s.isIsomorphic("paper", "title"))