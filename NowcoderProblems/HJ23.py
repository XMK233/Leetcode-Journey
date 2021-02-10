'''
https://www.nowcoder.com/practice/05182d328eb848dda7fdd5e029a56da9?tpId=37&tqId=21246&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。

示例1
输入
复制
abcdd
aabcddd
输出
复制
dd
aaddd



'''

Inf = []
while True:
    try:
        Inf.append(input())
    except:
        break

import collections
def deleteLeastAppearanceChars(string):
    newString = string
    counter = collections.defaultdict(int)
    ## 统计出现次数
    for c in string:
        counter[c] += 1
    ## 根据出现次数进行排序
    l = []
    for c in counter:
        l.append((c, counter[c]))
    l.sort(key=lambda x:x[1])
    ## 寻找出现次数最少的字符，然后去掉。
    leastTime = l[0][1]
    for i in range(len(l)):
        if l[i][1] > leastTime:
            break
        newString = newString.replace(l[i][0], "")
    return newString

for string in Inf:
    print(deleteLeastAppearanceChars(string))
