'''
[面试题 17.13. 恢复空格 - 力扣（LeetCode）](https://leetcode-cn.com/problems/re-space-lcci)

哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

 

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。


提示：


	0 <= len(sentence) <= 1000
	dictionary中总字符数不超过 150000。
	你可以认为dictionary和sentence中只包含小写字母。

动态规划思想.
dp数组存的是sentence从头开始, 到当前字符结尾的子串, 有多少未识别字符数量.
当遍历sentence到i这个地点的时候啊, 注意一下, 看一下以它结尾往前倒的子串, 有没有是字典里有的.
如果有的话, 就相应更新dp数组.
总的来说, 没有什么技术含量. 非常简单直白明了.
'''
class Solution:
    def respace(self, dictionary, sentence: str) -> int:
        if len(sentence) <= 0: return 0
        if len(dictionary) <= 0: return len(sentence)

        dp = [0] * (len(sentence) + 1)  # 最后一个0是哨兵 ## 我体会了这个哨兵的妙处. 因为一开始的时候i是0, 那么i-1=-1, 所以dp[i-1]就是数组的最后一个数字, 介个数字也就是哨兵了.
        for i in range(len(sentence)):
            dp[i] = dp[i - 1] + 1
            # 遍历所有单词，看能否和「以i为结尾的子串」一样
            for dic in dictionary:
                if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
                    dp[i] = min(dp[i], dp[i - len(dic)])
        return dp[-2]

# print(
#     Solution().respace(
# ["looked","just","like","her","brother"], "jesslookedjustliketimherbrother"
#     )
# )
l = [1, 2, 3, 4]
print(l[-1])

# 作者：dz-lee
# 链接：https://leetcode-cn.com/problems/re-space-lcci/solution/dpdong-tai-gui-hua-yi-li-jie-python-by-dz-lee/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。