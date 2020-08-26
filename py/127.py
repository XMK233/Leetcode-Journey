class Solution:
    # def changeOneLetter(self, wordA, wordB):
    #     ### 判断两个单词之间是不是只相差1
    #     differentLetterCount = 0
    #     for la, lb in zip(wordA, wordB):
    #         if la != lb:
    #             differentLetterCount += 1
    #     return differentLetterCount == 1

    # def allSimilarWords(self, beginWord, wordList):
    #     wordList_similar = []
    #     for word in wordList:
    #         if self.changeOneLetter(beginWord, word):
    #             wordList_similar.append(word)
    #     for word in wordList_similar:
    #         wordList.remove(word)
    #     return wordList_similar

    def allSimilarWords(self, word, wordListSet):
        wordLen = len(word)
        word_list = list(word)
        wordSimilar = []
        for i in range(wordLen):
            originChar = word_list[i]
            for k in range(26):
                word_list[i] = chr(ord('a') + k)
                nextWord = "".join(word_list)
                if nextWord in wordListSet:
                    wordSimilar.append(nextWord)
            word_list[i] = originChar
        for word in wordSimilar:
            if word in wordListSet:
                wordListSet.remove(word)
        return wordSimilar

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordListNew = wordList.copy()
        if beginWord in wordListNew:
            wordListNew.remove(beginWord)
        wordListNewSet = set(wordListNew)
        queue = [beginWord]
        level = 1
        lastWord = beginWord
        while len(queue) != 0:
            currentWord = queue.pop(0)
            queue.extend(self.allSimilarWords(currentWord, wordListNewSet))
            ### 如果换行了, 那么lastword就要更新了, level也要更新
            if currentWord == endWord:
                return level
            if currentWord == lastWord and len(queue) != 0:
                lastWord = queue[-1]
                level += 1
        return 0

# from typin import List
# from collections import dequeg
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         word_set = set(wordList)
#         if len(word_set) == 0 or endWord not in word_set:
#             return 0
#
#         if beginWord in word_set:
#             word_set.remove(beginWord)
#
#         queue = deque()
#         queue.append(beginWord)
#
#         visited = set(beginWord)
#
#         word_len = len(beginWord)
#         step = 1
#         while queue:
#             current_size = len(queue)
#             for i in range(current_size):
#                 word = queue.popleft()
#
#                 word_list = list(word)
#                 for j in range(word_len):
#                     origin_char = word_list[j]
#
#                     for k in range(26):
#                         word_list[j] = chr(ord('a') + k)
#                         next_word = ''.join(word_list)
#                         if next_word in word_set:
#                             if next_word == endWord:
#                                 return step + 1
#                             if next_word not in visited:
#                                 queue.append(next_word)
#                                 visited.add(next_word)
#                     word_list[j] = origin_char
#             step += 1
#         return 0

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/word-ladder/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

s = Solution()
print(
    s.ladderLength(
        "hit",
        "cog",
        ["hot","cog","dot","dog","hit","lot","log"]
    )
)
# print(s.changeOneLetter("leet", "lest"))