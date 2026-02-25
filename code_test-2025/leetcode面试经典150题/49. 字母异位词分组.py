'''中等
相关标签
premium lock icon
相关企业
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

解释：

在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
示例 2:

输入: strs = [""]

输出: [[""]]

示例 3:

输入: strs = ["a"]

输出: [["a"]]

 

提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母'''

from typing import List, Dict, Tuple
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 思路：把“字母异位词”转换为同一个“签名”，用哈希表按照签名分组
        # 这里的签名选择为：26 个小写字母的频次数组（再转成元组，作为 dict key）
        groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
        for s in strs:
            # 统计当前字符串中每个字母出现次数
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            # 频次数组转成不可变的元组，作为字典的键
            key = tuple(count)
            groups[key].append(s)
        # 将每个 key 对应的字符串列表收集为结果
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
    ]
    for strs in cases:
        print(f"input: {strs}")
        print(f"grouped: {sol.groupAnagrams(strs)}")
