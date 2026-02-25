'''给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

 

示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：

输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
 

提示：

1 <= haystack.length, needle.length <= 104
haystack 和 needle 仅由小写英文字符组成'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        在 haystack 中找出 needle 第一个匹配项的下标。
        如果 needle 不是 haystack 的一部分，则返回 -1。
        """
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        # 遍历 haystack，检查每一个可能的起始位置
        for i in range(n - m + 1):
            # 判断从 i 开始的子串是否匹配 needle
            # 注意：Python 的切片操作 haystack[i:i+m] 会创建新的字符串，
            # 虽然写起来简单，但在极长字符串下可能有性能开销。
            # 对于本题规模 (10^4)，这种 O(N*M) 的解法通常可以接受。
            if haystack[i : i + m] == needle:
                return i
                
        return -1

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1
    haystack1 = "sadbutsad"
    needle1 = "sad"
    print(f"Input: haystack = '{haystack1}', needle = '{needle1}'")
    print(f"Output: {sol.strStr(haystack1, needle1)}")  # 预期: 0
    
    # 测试用例 2
    haystack2 = "leetcode"
    needle2 = "leeto"
    print(f"Input: haystack = '{haystack2}', needle = '{needle2}'")
    print(f"Output: {sol.strStr(haystack2, needle2)}")  # 预期: -1
    
    # 测试用例 3
    haystack3 = "hello"
    needle3 = "ll"
    print(f"Input: haystack = '{haystack3}', needle = '{needle3}'")
    print(f"Output: {sol.strStr(haystack3, needle3)}")  # 预期: 2
