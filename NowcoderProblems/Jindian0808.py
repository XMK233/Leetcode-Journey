'''
[面试题 08.08. 有重复字符串的排列组合 - 力扣（LeetCode）](https://leetcode-cn.com/problems/permutation-ii-lcci)

有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

示例1:

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]


示例2:

 输入：S = "ab"
 输出：["ab", "ba"]


提示:


	字符都是英文字母。
	字符串长度在[1, 9]之间。

'''
import itertools
class Solution:
    def permutation(self, S: str):
        res_ = itertools.permutations([c for c in S], len(S))
        res = set(res_)
        res_real = []
        for r in res:
            res_real.append("".join(r))
        return res_real
