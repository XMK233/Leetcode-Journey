'''
https://www.nowcoder.com/practice/03ba8aeeef73400ca7a37a5f3370fe68?tpId=37&tqId=21250&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
定义一个单词的“兄弟单词”为：交换该单词字母顺序，而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如：ab和ba是兄弟单词。ab和ab则不是兄弟单词。
现在给定你n个单词，另外再给你一个单词str，让你寻找str的兄弟单词里，字典序第k大的那个单词是什么？
注意：字典中可能有重复单词。本题含有多组输入数据。
输入描述:
先输入单词的个数n，再输入n个单词。
再输入一个单词，为待查找的单词x
最后输入数字k
输出描述:
输出查找到x的兄弟单词的个数m
然后输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。
示例1
输入
复制
3 abc bca cab abc 1
输出
复制
2
bca

'''
def isBrothers(word1, word2):
    if len(word1) != len(word2): ## 这个if, 没考虑到过, 所以错了. 这个是一个错点.
        return False
    for c1, c2 in zip(
            sorted( [c for c in word1] ), sorted(  [c for c in word2]  )
    ):
        if c1 != c2:
            return False
    return True

print(
    isBrothers("dacbb", "a")
)

# items = input().split()
# numOfWords = int(items[0])
# order = int(items[-1])
# target = items[-2]
# words = items[1:1+numOfWords]
# bros = {}
# for word in words:
#     ## 自己不算
#     if target == word:
#         continue
#     ##
#     if isBrothers(word, target):
#         bros[word] = 1
# print(len(bros))
# answer = sorted(bros.keys())
# if order <= len(answer):
#     print(answer[order-1])


