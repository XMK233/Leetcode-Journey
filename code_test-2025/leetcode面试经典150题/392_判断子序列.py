#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
392. 判断子序列
简单

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true

示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false

提示：
0 <= s.length <= 100
0 <= t.length <= 10^4
两个字符串都只由小写字符组成。
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        方法1: 双指针法
        使用两个指针分别遍历s和t
        
        算法思路：
        1. 使用指针i遍历字符串s
        2. 使用指针j遍历字符串t
        3. 当s[i] == t[j]时，两个指针都向前移动
        4. 当s[i] != t[j]时，只有j指针向前移动
        5. 如果i能遍历完s，说明s是t的子序列
        
        时间复杂度: O(n) - n为t的长度
        空间复杂度: O(1) - 只使用了常数个额外变量
        """
        if not s:
            return True
        
        i = j = 0
        len_s, len_t = len(s), len(t)
        
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len_s
    
    def isSubsequence_v2(self, s: str, t: str) -> bool:
        """
        方法2: 使用内置函数
        利用Python的find函数来查找字符位置
        
        算法思路：
        1. 维护一个指针pos，表示在t中当前查找的位置
        2. 对于s中的每个字符，在t的pos位置之后查找
        3. 如果找不到，返回False
        4. 如果能找到，更新pos位置
        
        时间复杂度: O(n) - n为t的长度
        空间复杂度: O(1)
        """
        if not s:
            return True
        
        pos = -1  # 初始位置为-1，表示从开头开始查找
        
        for char in s:
            # 在t的pos+1位置之后查找char
            pos = t.find(char, pos + 1)
            if pos == -1:
                return False
        
        return True
    
    def isSubsequence_v3(self, s: str, t: str) -> bool:
        """
        方法3: 递归法
        使用递归的方式判断子序列
        
        时间复杂度: O(n) - n为t的长度
        空间复杂度: O(m) - m为s的长度（递归栈深度）
        """
        if not s:
            return True
        if not t:
            return False
        
        # 如果第一个字符匹配，递归判断剩余部分
        if s[0] == t[0]:
            return self.isSubsequence_v3(s[1:], t[1:])
        else:
            # 如果第一个字符不匹配，跳过t的第一个字符继续判断
            return self.isSubsequence_v3(s, t[1:])
    
    def isSubsequence_v4(self, s: str, t: str) -> bool:
        """
        方法4: 动态规划预处理（适用于大量查询的情况）
        预处理t字符串，记录每个位置之后各个字符第一次出现的位置
        
        算法思路：
        1. 预处理t字符串，创建一个dp数组
        2. dp[i][j]表示从位置i开始，字符j第一次出现的位置
        3. 查询时根据dp数组快速定位
        
        预处理时间复杂度: O(n * 26) - n为t的长度
        查询时间复杂度: O(m) - m为s的长度
        空间复杂度: O(n * 26)
        """
        if not s:
            return True
        
        n = len(t)
        # dp[i][j]表示从位置i开始，字符j第一次出现的位置
        dp = [[-1] * 26 for _ in range(n + 1)]
        
        # 从后往前填充dp数组
        for i in range(n - 1, -1, -1):
            # 复制下一行的信息
            for j in range(26):
                dp[i][j] = dp[i + 1][j]
            # 更新当前字符的信息
            char_idx = ord(t[i]) - ord('a')
            dp[i][char_idx] = i
        
        # 使用dp数组进行查询
        pos = 0  # 当前在t中的位置
        for char in s:
            char_idx = ord(char) - ord('a')
            # 在当前位置之后查找字符
            if dp[pos][char_idx] == -1:
                return False
            pos = dp[pos][char_idx] + 1
            if pos > n:
                return False
        
        return True

def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例1
    print("测试用例1:")
    s1, t1 = "abc", "ahbgdc"
    result1 = solution.isSubsequence(s1, t1)
    print(f"输入: s = '{s1}', t = '{t1}'")
    print(f"输出: {result1}")
    print(f"预期: True")
    print()
    
    # 测试用例2
    print("测试用例2:")
    s2, t2 = "axc", "ahbgdc"
    result2 = solution.isSubsequence(s2, t2)
    print(f"输入: s = '{s2}', t = '{t2}'")
    print(f"输出: {result2}")
    print(f"预期: False")
    print()
    
    # 测试用例3 - 空字符串
    print("测试用例3:")
    s3, t3 = "", "ahbgdc"
    result3 = solution.isSubsequence(s3, t3)
    print(f"输入: s = '{s3}', t = '{t3}'")
    print(f"输出: {result3}")
    print(f"预期: True")
    print()
    
    # 测试用例4 - s和t相同
    print("测试用例4:")
    s4, t4 = "abc", "abc"
    result4 = solution.isSubsequence(s4, t4)
    print(f"输入: s = '{s4}', t = '{t4}'")
    print(f"输出: {result4}")
    print(f"预期: True")
    print()
    
    # 测试用例5 - s比t长
    print("测试用例5:")
    s5, t5 = "abcd", "abc"
    result5 = solution.isSubsequence(s5, t5)
    print(f"输入: s = '{s5}', t = '{t5}'")
    print(f"输出: {result5}")
    print(f"预期: False")
    print()
    
    # 测试用例6 - 使用方法2
    print("测试用例6 - 使用方法2:")
    s6, t6 = "abc", "ahbgdc"
    result6 = solution.isSubsequence_v2(s6, t6)
    print(f"输入: s = '{s6}', t = '{t6}'")
    print(f"输出: {result6}")
    print(f"预期: True")
    print()
    
    # 测试用例7 - 使用方法3
    print("测试用例7 - 使用方法3:")
    s7, t7 = "abc", "ahbgdc"
    result7 = solution.isSubsequence_v3(s7, t7)
    print(f"输入: s = '{s7}', t = '{t7}'")
    print(f"输出: {result7}")
    print(f"预期: True")
    print()
    
    # 测试用例8 - 使用方法4
    print("测试用例8 - 使用方法4:")
    s8, t8 = "abc", "ahbgdc"
    result8 = solution.isSubsequence_v4(s8, t8)
    print(f"输入: s = '{s8}', t = '{t8}'")
    print(f"输出: {result8}")
    print(f"预期: True")

if __name__ == "__main__":
    test_solution()