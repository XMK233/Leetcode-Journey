# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c466d480d20c4c7c9d322d12ca7955ac?tpId=117&&tqId=37732&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出两个字符串 SS 和 TT，要求在O(n)O(n)的时间复杂度内在 SS 中找出最短的包含 TT 中所有字符的子串。
例如：

S ="XDOYEZODEYXNZ"S="XDOYEZODEYXNZ"
T ="XYZ"T="XYZ"
找出的最短子串为"YXNZ""YXNZ".

注意：
如果 SS 中没有包含 TT 中所有字符的子串，返回空字符串 “”；
满足条件的子串可能有很多，但是题目保证满足条件的最短的子串唯一。

示例1
输入
复制
"XDOYEZODEYXNZ","XYZ"
返回值
复制
"YXNZ"

不知道是怎么做出来的. 也不知道是不是抄的了.
'''
class Solution:
    def minWindow(self , S , T ):
        ## 直接处理掉空串的情况
        if T == "":
            return ""
        # write code here
        numOfTargetChar = {}
        for c in T:
            if c not in numOfTargetChar:
                numOfTargetChar[c] = 1
            else:
                numOfTargetChar[c] += 1
        numOfCurrentlyMet = {}
        for c in T:
            numOfCurrentlyMet[c] = 0
        howManyToGo = len(set(T)) ## 这边假定T里面的字符串全都不重复

        head, tail = 0, 0
        minSubString = "_" * (len(S) + 1) ## 这个初始长度, 绝对大于S的任何子串吧.

        while tail < len(S):
            while howManyToGo > 0 and tail < len(S):
                if S[tail] in T:
                    ## howmanytogo指的是T中还有多少个字符还没在S中找到
                    if numOfCurrentlyMet[S[tail]] == numOfTargetChar[S[tail]] - 1: ## 这个条件说明啊, 字符 S[tail] 是第一次被找到.
                    # if numOfCurrentlyMet[S[tail]] == 0:  ## 这个条件说明啊, 字符 S[tail] 是第一次被找到.
                        howManyToGo -= 1
                    numOfCurrentlyMet[S[tail]] += 1  ## 这里指的是, 这个S[tail]字符迄今为止遇到了几次了. 因为可能遇到不止一次嘛, 就记一下次数.
                # else:
                #     pass
                if howManyToGo == 0:
                    break
                else:
                    tail += 1

            if tail >= len(S):
                break

            while S[head] not in T:
                head += 1
            curSubString = S[head:tail + 1]
            if len(curSubString) < len(minSubString):
                minSubString = curSubString

            numOfCurrentlyMet[S[head]] -= 1
            # if numOfCurrentlyMet[S[head]] == 0:## 如果有一个T中的字符, 不再在[head + 1, tail]之间了, 那么这个字符的计数就要扣掉.
            if numOfCurrentlyMet[S[head]] < numOfTargetChar[S[head]]:
                howManyToGo += 1
                tail += 1 ## tail也要相应地往后移动一位, 开始新的征程.
            head += 1

        # if tail >= len(S):
        return "" if len(minSubString) == (len(S) + 1) else minSubString