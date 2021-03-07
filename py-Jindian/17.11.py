'''
[面试题 17.11. 单词距离 - 力扣（LeetCode）](https://leetcode-cn.com/problems/find-closest-lcci)

有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：

输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1

提示：


	words.length <= 100000

'''
'''
非常简洁明了. 就是双指针, 然后一个指针指向word1, 另一个指向word2, 然后随时记录两个指针之间的差值的最小值就好了. 
'''
# 方法2：双指针
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = float("-inf"), float("inf")
        res = len(words)
        for idx, word in enumerate(words):
            if word == word1:
                idx1 = idx
            elif word == word2:
                idx2 = idx
            res = min(res, abs(idx1-idx2))
        return res

# 作者：821218213
# 链接：https://leetcode-cn.com/problems/find-closest-lcci/solution/mian-shi-ti-1711yong-zi-dian-ji-lu-dan-ci-chu-xian/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。