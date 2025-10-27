"""
3. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
- 0 <= s.length <= 5 * 10^4
- s 由英文字母、数字、符号和空格组成
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        方法1: 滑动窗口 + 哈希集合
        使用滑动窗口和哈希集合来跟踪窗口中的字符
        
        算法思路：
        1. 使用两个指针left和right表示滑动窗口的左右边界
        2. 使用集合来存储当前窗口中的字符
        3. 如果s[right]不在集合中，将其加入集合并更新最大长度
        4. 如果s[right]已在集合中，移动left指针直到重复字符被移除
        
        时间复杂度: O(n) - n为字符串长度，每个字符最多被访问两次
        空间复杂度: O(min(m, n)) - m为字符集大小，最坏情况下需要存储所有不同字符
        """
        if not s:
            return 0
        
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # 如果当前字符已经在集合中，移动左指针
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # 将当前字符加入集合
            char_set.add(s[right])
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        """
        方法2: 滑动窗口 + 哈希表优化
        使用哈希表存储字符的索引，可以快速定位重复字符的位置
        
        算法思路：
        1. 使用字典存储字符及其最新出现的索引
        2. 当遇到重复字符时，直接将left指针跳到重复字符的下一个位置
        3. 这样可以避免逐个移除字符的低效操作
        
        时间复杂度: O(n) - 每个字符只需遍历一次
        空间复杂度: O(min(m, n)) - m为字符集大小
        """
        if not s:
            return 0
        
        char_index = {}  # 存储字符及其最新出现的索引
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # 如果当前字符已经在字典中，且其位置在当前窗口内
            if s[right] in char_index and char_index[s[right]] >= left:
                # 直接将left指针跳到重复字符的下一个位置
                left = char_index[s[right]] + 1
            
            # 更新字符的索引
            char_index[s[right]] = right
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def lengthOfLongestSubstring_v3(self, s: str) -> int:
        """
        方法3: 优化的滑动窗口（数组代替哈希表）
        由于题目说明字符串只包含ASCII字符，可以使用数组来提高效率
        
        算法思路：
        1. 使用长度为256的数组来存储每个ASCII字符的最新位置
        2. 数组的索引代表字符的ASCII码，值代表该字符最新出现的位置
        3. 这样可以避免哈希表的操作开销
        
        时间复杂度: O(n)
        空间复杂度: O(1) - 固定大小的数组
        """
        if not s:
            return 0
        
        # ASCII字符集大小为256
        char_index = [-1] * 256  # 初始化所有字符的位置为-1
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # 获取当前字符的ASCII码
            ascii_val = ord(s[right])
            
            # 如果字符之前出现过且位置在当前窗口内
            if char_index[ascii_val] >= left:
                # 移动left指针到重复字符的下一个位置
                left = char_index[ascii_val] + 1
            
            # 更新字符的最新位置
            char_index[ascii_val] = right
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length


def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例
    test_cases = [
        ("abcabcbb", 3),      # 基本测试："abc"是最长子串
        ("bbbbb", 1),         # 所有字符相同："b"
        ("pwwkew", 3),        # 复杂情况："wke"
        ("", 0),              # 空字符串
        ("a", 1),             # 单个字符
        ("ab", 2),            # 两个不同字符
        ("aa", 1),            # 两个相同字符
        ("dvdf", 3),          # 特殊情况："vdf"
        ("anviaj", 5),        # 特殊情况："nviaj"
        ("abcdefghijklmnopqrstuvwxyz", 26),  # 所有字母都不同
    ]
    
    print("测试无重复字符的最长子串问题：")
    print("=" * 50)
    
    for i, (s, expected) in enumerate(test_cases, 1):
        result1 = solution.lengthOfLongestSubstring(s)
        result2 = solution.lengthOfLongestSubstring_v2(s)
        result3 = solution.lengthOfLongestSubstring_v3(s)
        
        print(f"测试用例 {i}: '{s}'")
        print(f"期望结果: {expected}")
        print(f"方法1结果: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"方法2结果: {result2} {'✓' if result2 == expected else '✗'}")
        print(f"方法3结果: {result3} {'✓' if result3 == expected else '✗'}")
        print("-" * 30)


if __name__ == "__main__":
    test_solution()