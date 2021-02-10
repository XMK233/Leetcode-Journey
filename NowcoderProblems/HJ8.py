'''
https://www.nowcoder.com/practice/de044e89123f4a7482bd2b214a685201?tpId=37&tqId=21231&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
复制
4
0 1
0 2
1 2
3 4
输出
复制
0 3
1 2
3 4

'''

import collections
m = collections.defaultdict(int)

numOfLines = int(input())

for __ in range(numOfLines):
    _ = input()
    nums = [int(x) for x in _.split()]
    key = nums[0]
    value = nums[1]
    m[key] += value
keys = sorted(m.keys())
for key in keys:
    print(key, m[key])