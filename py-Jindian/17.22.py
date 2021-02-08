'''
[面试题 17.22. 单词转换 - 力扣（LeetCode）](https://leetcode-cn.com/problems/word-transformer-lcci)

给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。

编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]


示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
'''
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        # DFS
        hashmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hashmap[word[:i] + '*' + word[i + 1:]].append(word)
        stack = [beginWord]
        w_dict = {beginWord: [beginWord]}
        while stack:
            word = stack.pop()
            if word == endWord:
                return w_dict[word]
            for i in range(len(word)):
                if word[:i] + '*' + word[i + 1:] in hashmap:
                    for tmp in hashmap[word[:i] + '*' + word[i + 1:]]:
                        if tmp not in w_dict:
                            w_dict[tmp] = w_dict[word] + [tmp]
                            stack.append(tmp)
        return []

s = Solution()
print(s.findLadders(
    "hit", "cog",
    ["hot","dot","dog","lot","log","cog"]
))

# 作者：rao-zhi-cheng-shang-2
# 链接：https://leetcode-cn.com/problems/word-transformer-lcci/solution/python3-dfs-bfs-jian-zhi-by-rao-zhi-cheng-shang-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。