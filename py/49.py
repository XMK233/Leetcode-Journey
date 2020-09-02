import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res[sorted_str].append(string)
        return res.values()

### 哈哈哈, 真的没有花活. 就是非常普通的思想.
### 如果每一个字符串的长度都不太长的话, 直接把字符串给他排序了, 然后弄到dict里面.
### 卧槽. 事件一切要是都可以这么简单, 相逢何必曾相识啊.