# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/6d29638c85bb4ffd80c020fe244baf11?tpId=117&&tqId=37798&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

参考 https://blog.csdn.net/hrn1216/article/details/51534607 的思路，很清晰。
但是LCS()不能AC，感觉牛客网上抄来的答案LCS1()也不太靠谱，所以还是以后慢慢实现吧。
'''
class Solution:
    def LCS(self , s1 , s2 ):
        text1 = s1
        text2 = s2
        if not text1 or not text2:
            return 0
        res = []
        dp = [0 for _ in range(len(text2)+1)]
        for i in range(1, len(text1)+1):
            pre = 0
            for j in range(1, len(text2)+1):
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                pre = temp
        return dp[-1]

    # 作者：jue-qiang-zha-zha
    # 链接：https://leetcode-cn.com/problems/longest-common-subsequence/solution/1143-zui-chang-gong-gong-zi-xu-lie-dong-akex6/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    def LCS1(self, s1, s2):
        # write code here
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            s1, s2 = s2, s1
        max_len = 0
        res = ""
        for i in range(n1):
            if s1[i - max_len: i + 1] in s2:
                res += s1[i - max_len: i + 1]
                max_len += 1
        if len(res) == 0:
            return "-1"
        else:
            return res

print(
    Solution().LCS("1A2C3D4B56","B1D23CA45B6A")
)
