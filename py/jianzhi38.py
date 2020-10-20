class Solution:
    def permutation(self, s: str):
        if s == "":
            return []
        elif len(s) == 1:
            return [s]
        ##
        res = []
        for i in range(len(s)):
            if i == 0:
                tailPart = s[1:]
                subPermutation = self.permutation(tailPart)
                res.extend([s[0] + _ for _ in subPermutation])
            elif i == len(s) - 1:
                headPart = s[0:i]
                subPermutation = self.permutation(headPart)
                res.extend([s[-1] + _ for _ in subPermutation])
            else:
                curChar = s[i]
                headPart = s[0:i]
                tailPart = s[i+1:]
                subPermutation = self.permutation(headPart + tailPart)
                res.extend([curChar + _ for _ in subPermutation])
        return list(set(res))

s = Solution()
print(s.permutation("abc"))

