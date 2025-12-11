from typing import List

'''简单
相关标签
premium lock icon
相关企业
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 

提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 如果非空，则仅由小写英文字母组成'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 如果字符串数组为空，直接返回空字符串
        if not strs:
            return ""
        
        # 以第一个字符串为基准
        prefix = ""
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            # 检查所有其他字符串是否在当前位置有相同的字符
            for string in strs[1:]:
                # 如果超出其他字符串长度或字符不匹配，返回当前前缀
                if i >= len(string) or string[i] != current_char:
                    return prefix
            # 所有字符串在当前位置都匹配，添加到前缀
            prefix += current_char
        
        return prefix

# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    strs1 = ["flower", "flow", "flight"]
    print(f"输入: strs = {strs1}, 输出: '{solution.longestCommonPrefix(strs1)}', 预期: 'fl'")
    
    # 测试用例2
    strs2 = ["dog", "racecar", "car"]
    print(f"输入: strs = {strs2}, 输出: '{solution.longestCommonPrefix(strs2)}', 预期: ''")
    
    # 测试用例3
    strs3 = ["apple", "app", "application"]
    print(f"输入: strs = {strs3}, 输出: '{solution.longestCommonPrefix(strs3)}', 预期: 'app'")
    
    # 测试用例4
    strs4 = ["a"]
    print(f"输入: strs = {strs4}, 输出: '{solution.longestCommonPrefix(strs4)}', 预期: 'a'")
    
    # 测试用例5
    strs5 = ["", "b"]
    print(f"输入: strs = {strs5}, 输出: '{solution.longestCommonPrefix(strs5)}', 预期: ''")
