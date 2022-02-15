class Solution:
    def solve(self, s: str, t: str) -> str:
        # write code here
        if not s:
            return t
        if not t:
            return s

        ls = len(s)
        lt = len(t)
        max_len = max(ls, lt)
        ## 我感觉技巧点在于这里，就是用前置0给他补齐。
        sl = s.zfill(max_len)
        tl = t.zfill(max_len)

        full = 0
        res = ""

        for i in range(max_len-1, -1, -1):
            sum_of_two = int(sl[i]) + int(tl[i]) + full
            if sum_of_two >= 10:
                res = str(sum_of_two - 10) + res
                full = 1
            else:
                res = str(sum_of_two) + res
                full = 0
        if full == 1:
            res = "1" + res
        return res
print(Solution().solve("9","99999999999999999999999999999999999999999999999999999999999994"))

