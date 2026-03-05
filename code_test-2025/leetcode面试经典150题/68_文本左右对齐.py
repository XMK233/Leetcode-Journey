'''困难
相关标签
premium lock icon
相关企业
给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

注意:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
 

示例 1:

输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

提示:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] 由小写英文字母和符号组成
1 <= maxWidth <= 100
words[i].length <= maxWidth
'''

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 思路：按行贪心装单词，再根据“是否为最后一行 / 每行单词数”决定如何分配空格
        res: List[str] = []
        i = 0
        n = len(words)
        while i < n:
            # 1. 贪心确定当前行能放哪些单词：尽量多放
            line_len = len(words[i])  # 当前行单词字符总长度（不含空格）
            j = i + 1
            # 尝试加入更多单词，保证：单词长度 + 至少一个空格的数量 <= maxWidth
            while j < n and line_len + 1 + len(words[j]) + (j - i - 1) <= maxWidth:
                # (j - i - 1) 是之前已经加入的空格数，这里统一写在一条公式中
                line_len += len(words[j])
                j += 1

            # 当前行包含的单词下标为 [i, j-1]
            num_words = j - i
            is_last_line = (j == n)

            # 2. 构造这一行
            if num_words == 1 or is_last_line:
                # 情况 A：只有一个单词，或者最后一行 -> 左对齐
                line = words[i]
                for k in range(i + 1, j):
                    line += " " + words[k]  # 单词之间一个空格
                # 末尾补足空格到 maxWidth
                line += " " * (maxWidth - len(line))
            else:
                # 情况 B：中间行，且有多个单词 -> 两端对齐，尽量均匀分配空格
                total_spaces = maxWidth - line_len          # 总空格数
                gaps = num_words - 1                        # 间隙个数
                space_each = total_spaces // gaps           # 每个间隙至少的空格数
                extra = total_spaces % gaps                 # 前 extra 个间隙多一个空格

                line_parts: List[str] = []
                for k in range(i, j):
                    line_parts.append(words[k])
                    if k < j - 1:  # 不是最后一个单词，就要加空格
                        # 如果还有“多出来”的空格，就先分配到左边的间隙
                        spaces = space_each + (1 if extra > 0 else 0)
                        if extra > 0:
                            extra -= 1
                        line_parts.append(" " * spaces)
                line = "".join(line_parts)

            res.append(line)
            i = j

        return res


if __name__ == "__main__":
    sol = Solution()
    ws1 = ["This", "is", "an", "example", "of", "text", "justification."]
    for row in sol.fullJustify(ws1, 16):
        print(f"'{row}'", len(row))
