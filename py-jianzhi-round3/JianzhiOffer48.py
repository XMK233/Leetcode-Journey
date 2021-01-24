'''
[剑指 Offer 48. 最长不含重复字符的子字符串 - 力扣（LeetCode）](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof)

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


 

提示：


	s.length <= 40000


注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
'''
'''
# 利用hash表；还有就是一定要想到好的测试用例。"tmmzuxt"和"abcabcbb"这两种测试用例说明了两种情况。
#
# Python。
#
# 关键点：只需遍历一遍就行了。不要硬性穷举。
# 利用hash表来判断字符是否重复，用空间换时间。
# 如果发现有一个字符重复出现了，那么新的最大子串只可能从（重复的字符上一次出现的地方的后一个地方，这个地方我们称为head）开始。
# 如果head之后遍历到一个重复字符串重复了，但是上一次这个字符串出现的位置在head之前，
# 那么就说明这个“重复字符”实际上并不是真正的重复字符，应当作为新出现的字符来看待，只
# 要像普通字符串那样更新就好了。
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        longest = 0
        dic = {}  # 存放的是字符，以及字符在字符串中的序号。

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= head:  # 如果这个字符是重复的字符，并且上一次出现在head之后，
                head = dic[s[i]] + 1  # 才需要移动head
            dic[s[i]] = i  # 否则一律按新出现字符来看待。
            longest = max((i - head + 1), longest) # 看看最大长度有没有更新

        return longest

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()