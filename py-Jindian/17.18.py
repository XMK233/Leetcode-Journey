'''
[面试题 17.18. 最短超串 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shortest-supersequence-lcci)

假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

示例 1:

输入:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
输出: [7,10]

示例 2:

输入:
big = [1,2,3]
small = [4]
输出: []

提示：


	big.length <= 100000
	1 <= small.length <= 100000

'''

# class Solution:
#     def shortestSeq(self, S, T):
#         ## 直接处理掉空串的情况
#         if len(T) == 0:
#             return []
#         # write code here
#         numOfTargetChar = {}
#         for c in T:
#             if c not in numOfTargetChar:
#                 numOfTargetChar[c] = 1
#             else:
#                 numOfTargetChar[c] += 1
#         numOfCurrentlyMet = {}
#         for c in T:
#             numOfCurrentlyMet[c] = 0
#         howManyToGo = len(set(T)) ## 这边假定T里面的字符串全都不重复
#
#         head, tail = 0, 0
#         tgtHead, tgtTail = 0, 0
#         minSubString = [-1] * (len(S) + 1) ##"_" * (len(S) + 1) ## 这个初始长度, 绝对大于S的任何子串吧.
#
#         while tail < len(S):
#             while howManyToGo > 0 and tail < len(S):
#                 if S[tail] in T:
#                     ## howmanytogo指的是T中还有多少个字符还没在S中找到
#                     if numOfCurrentlyMet[S[tail]] == numOfTargetChar[S[tail]] - 1: ## 这个条件说明啊, 字符 S[tail] 是第一次被找到.
#                     # if numOfCurrentlyMet[S[tail]] == 0:  ## 这个条件说明啊, 字符 S[tail] 是第一次被找到.
#                         howManyToGo -= 1
#                     numOfCurrentlyMet[S[tail]] += 1  ## 这里指的是, 这个S[tail]字符迄今为止遇到了几次了. 因为可能遇到不止一次嘛, 就记一下次数.
#                 # else:
#                 #     pass
#                 if howManyToGo == 0:
#                     break
#                 else:
#                     tail += 1
#
#             if tail >= len(S):
#                 break
#
#             while S[head] not in T:
#                 head += 1
#             curSubString = S[head:tail + 1]
#             if len(curSubString) < len(minSubString):
#                 minSubString = curSubString
#                 tgtHead = head
#                 tgtTail = tail
#
#             numOfCurrentlyMet[S[head]] -= 1
#             # if numOfCurrentlyMet[S[head]] == 0:## 如果有一个T中的字符, 不再在[head + 1, tail]之间了, 那么这个字符的计数就要扣掉.
#             if numOfCurrentlyMet[S[head]] < numOfTargetChar[S[head]]:
#                 howManyToGo += 1
#                 tail += 1 ## tail也要相应地往后移动一位, 开始新的征程.
#             head += 1
#
#         # if tail >= len(S):
#         return [] if len(minSubString) == (len(S) + 1) else [tgtHead, tgtTail]#minSubString
#
# print(
#     Solution().shortestSeq(
#         [1, 2, 3],
#         [4]
#     )
# )

import collections
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        need = collections.Counter(small)
        needCnt = n_s = len(small)
        i = 0
        res = (0, len(big)+1)
        for j,c in enumerate(big):
            if need[c] > 0:
                needCnt -= 1    # 不在t中的字符默认是0，所以大于零的一定是t里的字符
            need[c] -= 1        # 当c出现次数超过所需次数时，need[c]<0，所以needcnt不会小于0
            if needCnt == 0:    # 步骤一：滑动窗口包含了所有T元素
                while True:     # 步骤二：增加i，排除多余元素
                    c = big[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j-i < res[1]-res[0]:   #记录结果
                    res =[i,j]
                    if j - i == n_s:
                        return res
                need[big[i]] += 1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return [] if res[1] > len(big) else res

## 我自己在牛客网的NC28里面做过一次. NC28里面的题目更复杂, 因为T是有重复元素的. LC的题目极其类似, 但是这里的T没有重复.
## 所以这一点上, 就已经不太一样了. 我用NC28的方法去求解, 得到的结果并不好, 有一些样例是会超时限的.

# # 作者：joeylin-m
# # 链接：https://leetcode-cn.com/problems/shortest-supersequence-lcci/solution/he-0076zui-xiao-fu-gai-zi-chuan-lei-si-d-naat/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。