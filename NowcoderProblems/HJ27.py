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

items = input().split()
# items = '''473 bb daccb caddd bddc c baa adb ad abbcb cdaa abab a abcc ddcbd cadcc cdacd aaa a b acccd bbb dacc cc acbdd bcbb ba bacaa adda acd aaad d ab acac bc dabab abcd aacba aba daa bb ad cddab a bbaa aacad cdac acbcc cada bacd adcad cdadc bcbcc aa b acd cbaac ddcd ccb dac a dac adbcb bcda dda a ab ca dd d abd a dbb ccabd bdddd abd adc aaa baccb ccdcd a da c cadc dcdbd d aa bb a cac c ad adb ca cdcc cadd dddca d cba cb caab caa dd cd bca abc cdaa cdb bad dad bda d ddbc dab baaa adaac b a dbccd bd b bdad cdacd baa ac ddcad d bb acc aa cd cbdbb bbbcb a cc aacc c aadc dbcd a bca dd abbb ccdcd ccd ab d a a dadcd dbd bcaa c cda b ddab caaaa cdcdb b acbc ccaa dabca dcd b ba dbcc da bdbcc ab abaca bb cddc caca da dadba accdd bdac dbcd bcbbd ab bd ccb ddaa aa b b d bddd cabac aaba ab ccdb db abbd ada bdadb c abba dd cdb bca cccda badba abaa ac aabad db ccbad bddd ada dba acba b bc dd bbbbd cc cbdd cd abcaa bb ddaca acadb bbbb bddcc bdada aaa bcbda c aaa aadd cdddc adb cdbab c cbca bb aacab acdb bbdab b acbda cbdcd bda bacdc db d adcbd bccc c aaa cdd bdcd bac a aaab ddbb cd ccdbb addcc cdc c ca baadc addba dbdbd dba bbdda bcb c cdad aacac dcada cb aaad a cccab caca aad bbb dd b babbb cba bdaca db bacd bc bcbda cdda bcccd bdcda bdbcd adb cbcb a c bacba abbb adab adab b b d bca badbc baa cdb b abc aabb b d c cdab cacda d cdcda adcdc bcc bbccd b adb caba cbaaa aadb dcc add bcac bacbd bb a b c cabaa c caad c aa bcc ccab ddc dadca cdcba aaba dabbd dcb a bddb bb a c c cbc ccd dd a cabbb b caadb cb dca cbb ddaa bcadc dab a bbda cd bc ccad bbd ab c acddd cdd dbbbb daaab abbb cabc add ca caa bbbb dcab daaaa baca dcd ccacb ba bddaa acac dbcc bcc cbbcc b abba daa dbab bcca ba aa d dcdc d dcaa cbcda bd b ccbcb baa dcacd d c cbda baba d abb c cbdc da dbbb cd aabc dadc b a ddb c ddd ccdc ccd cba dbaac dcccd ddbac dbbdd bad bcdd cb dac dccd d a acdd d c cb b bcbb c a aca bcba d d bbdbc d c dabad ccca dc adb ddb dcdd dba ad ddaba c ac ddac bbbd cd a dacbb 1'''.split()
# items = "2 bcbda bcbda dacbb 1".split()
numOfWords = int(items[0])
order = int(items[-1])
target = items[-2]
words = items[1: 1+numOfWords] ## 之前一直ac不了是因为这里我给它set(words)操作了一波, 属于画蛇添足.
bros_l = []
target_sorted = "".join(sorted(target))
for word in words:
    ## 自己不算
    if target == word:
        continue
    ##
    if isBrothers(word, target):
        # bros[word] = 1
        bros_l.append(word)
bros_l.sort()
print(len(bros_l))
if order <= len(bros_l):
    print(bros_l[order-1])

# from collections import defaultdict
# dd = defaultdict(list)
# a = items
# # words是输入的单词，lookup是要查找的单词，num是要查找兄弟单词的索引，brothers是找到的兄弟单词列表
# words, lookup, num, brothers = a[1:1 + int(a[0])], a[-2], int(a[-1]), []
# for i in words:
#     dd["".join(sorted(i))].append(i)
# for i in dd["".join(sorted(lookup))]:
#     if i != lookup: brothers.append(i)
# # 下面这两行坑的老子调了半个小时。
# print(len(brothers))
# if brothers and num <= len(brothers):
#     print(sorted(brothers)[num - 1])
# print(sorted(brothers))


