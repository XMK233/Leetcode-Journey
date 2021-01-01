'''
[剑指 Offer 05. 替换空格 - 力扣（LeetCode）](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof)

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

 

限制：

0 <= s 的长度 <= 10000
'''
'''
参考 https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/mian-shi-ti-05-ti-huan-kong-ge-ji-jian-qing-xi-tu-/
其实就是先计算扩充后的数组的长度, 然后从原数组的末尾开始倒着把一个一个字符给它填到新的数组里面去.
如果遍历到空格, 就把0, 2, %相继填入就好了.

如果使用python, 完全可以直接用最简单的方式.
'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")

s = Solution()
print(s.replaceSpace("We are happy."))



