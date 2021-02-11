'''
https://www.nowcoder.com/practice/b4525d1d84934cf280439aeecc36f4af?tpId=117&tqId=37789&rp=1&ru=%2Fta%2Fjob-code-high&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

题目描述
对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。

给定字符串A以及它的长度n，请返回最长回文子串的长度。

示例1
输入
复制
"abc1234321ab",12
返回值
复制
7

'''


## 从中间往两边扩散，看符不符合回文串的要求。
class Palindrome:
    def getLongestPalindrome(self, A, n):
        def func(A, left, right):
            while left >= 0 and right < n and A[left] == A[right]:
                left -= 1
                right += 1
            return right - left - 1

        res = 0
        for i in range(n - 1):
            res = max(res, func(A, i, i), func(A, i, i + 1))
        return res


## 以下是法2，据说复杂度只有O(n)：
# class Palindrome:
#     def getLongestPalindrome(self, A, n):
#         if n <= 1: return n
#         # 每个字符之间插入 #
#         ss = '$#' + '#'.join([x for x in A]) + '#`'
#         p = [1] * len(ss)
#         center = 0
#         mx = 0
#         max_str = ''
#         for i in range(1, len(p)-1):
#             if i < mx:
#                 j = 2 * center - i # i 关于 center 的对称点
#                 p[i] = min(p[j],mx-i)
#             # 尝试继续向两边扩展，更新 p[i]
#             while ss[i - p[i] ] == ss[i + p[i] ]: # 不必判断是否溢出，因为首位均有特殊字符，肯定会退出
#                 p[i] += 1
#             # 更新中心
#             if i + p[i] - 1 > mx:
#                 mx = i + p[i] - 1
#                 center = i
#             # 更新最长串
#             if 2 * p[i]-1 > len(max_str):
#                 max_str = ss[i - p[i]+1 : i + p[i]]
#         maxLen = len(max_str.replace('#', ''))
#         return maxLen