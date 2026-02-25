'''困难
相关标签
premium lock icon
相关企业
给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

 s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。

 

示例 1：

输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。
示例 2：

输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
所以我们返回一个空数组。
示例 3：

输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
 

提示：

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] 和 s 由小写英文字母组成'''

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []
            
        word_counts = Counter(words)
        result = []
        
        # 遍历所有可能的起始偏移量 (0 到 word_len - 1)
        # 这样可以将问题分解为 word_len 个独立的滑动窗口问题

        # 为什么要按 word_len 遍历 offset？
        # 题目有两个关键条件：
        # - 所有单词 words[i] 的长度都相同，比如都是 word_len = 3 。
        # - 串联子串要求是若干个单词首尾相连，中间不能断，也不能有半个单词。
        # 所以，任何合法的起始下标 start 都必须满足：
        # - 从 start 开始，每次往右走 word_len 个字符，恰好能走出一串完整的单词序列；
        # - 换句话说，候选的位置都是按 word_len 对齐的块起点。
        # 于是我们就可以把字符串看成是「按 word_len 切块」后的一维数组，只不过：
        # - 有 3 种切法（对于 word_len = 3 ）：
        # - offset = 0: [s[0:3], s[3:6], s[6:9], ...]
        # - offset = 1: [s[1:4], s[4:7], s[7:10], ...]
        # - offset = 2: [s[2:5], s[5:8], s[8:11], ...]
        # - 每一种切法对应 for i in range(word_len) 里的一个 i 。

        for i in range(word_len):
            left = i
            right = i
            window_counts = Counter()
            count = 0
            
            # 滑动窗口
            while right + word_len <= s_len:
                # 获取右侧单词
                w = s[right : right + word_len]
                right += word_len
                
                if w not in word_counts:
                    # 如果遇到不在 words 中的单词，重置窗口
                    window_counts.clear()
                    count = 0
                    left = right
                else:
                    window_counts[w] += 1
                    count += 1
                    
                    # 如果当前单词数量超过了 words 中的数量，收缩左侧
                    while window_counts[w] > word_counts[w]:
                        left_w = s[left : left + word_len]
                        left += word_len
                        window_counts[left_w] -= 1
                        count -= 1
                    
                    # 如果匹配的单词总数等于 words 中的单词总数，记录起始位置
                    if count == num_words:
                        result.append(left)
        
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # 示例 1
    s1 = "barfoothefoobarman"
    words1 = ["foo","bar"]
    print(f"Test 1: {sol.findSubstring(s1, words1)}") # Expected: [0, 9]

    # 示例 2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word","good","best","word"]
    print(f"Test 2: {sol.findSubstring(s2, words2)}") # Expected: []

    # 示例 3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar","foo","the"]
    print(f"Test 3: {sol.findSubstring(s3, words3)}") # Expected: [6, 9, 12]
