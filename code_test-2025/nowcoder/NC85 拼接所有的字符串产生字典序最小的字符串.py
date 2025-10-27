#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param strs string字符串一维数组 the strings
# @return string字符串
## 思路：序列要按照字典序来排布，这样组合起来才是字典序最小的组合。
## 但是，字典序最小的组合有点问题啊，比如如果bca和bc，谁应该排前面呢？肯定是bca要排序在前面。
## 可是默认的方法基本上都认定bc小于bca。所以可能得重新设计一下比大小的方法。
## 假设字符串不一样长，就可能比较复杂，比如说你要不要在短的后面补一下，这种。
## 如果补的话，怎么补呢，比如bca应该比bc小，那么bcd是不是又比bcd更大了呢？那你如何判断后面多出来的部分会对大小判断造成什么影响呢？
## 所以好的解决办法就是将两个字符串分别前后拼接起来看结果。比如对比一下bcabc bcbca哪个更小，用更小的那个来判断原来两个字符串的大小。

from functools import cmp_to_key
def numeric_compare(x, y):
    if x + y < y + x:
        return -1
    elif x + y > y+x:
        return 1
    else:
        return 0
class Solution:
    def minString(self , strs) -> str:
        # write code here

        return "".join(
            sorted(
                strs,
                key=cmp_to_key(numeric_compare)
            )
        )

print(
    # "abc" > "ab"
Solution().minString(["bca","bc"])
)