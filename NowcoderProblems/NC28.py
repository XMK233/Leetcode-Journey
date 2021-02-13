'''
https://www.nowcoder.com/practice/c466d480d20c4c7c9d322d12ca7955ac?tpId=117&tqId=37732&rp=1&ru=%2Fta%2Fjob-code-high&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

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

使用滑动窗口法.

以S = "ADOBECODEBANC", T = "ABC"为例，然后按照如图所示的规律滑动窗口
首先, head和tail都在0位置.
然后tail一直往右走, 直到head-tail这一段包含了所有的T中的字符. 如果T中字符有重复, 还得另外考虑.
    这里有点微妙.
    numOfTargetChar 指的是, T中各个字符需要几个. 例如, 假设T中"A"有俩, 那么numOfTargetChar[A] = 2
    numOfCurrentlyMet 指的是, tail遍历到现在, 已经遇上了几个T中字符. 例如迄今遇上过3个A, 那就numOfCurrentlyMet[A] = 3酱紫.
    howManyToGo 指的是不同的字符, 还有多少个没有找齐. 比如假设T是AABC, 在S中找到B有1个, A有1个, C尚未找到, 那么A与C都尚未找齐, 那么howManyToGo就是2.
    如果某一个numOfCurrentlyMet[T中字符] >= numOfTargetChar[T中字符], 说明这个T中字符已经找齐, 那么howManyToGo 就要减1.
然后head一直往右走, 直到head遇到一个T中字符串, 停下来.
然后, head-tail这一段看看是不是目前的最优解. 如果是, 就记录下来.
然后, head往右走一格, 那么原来的head对应的字符在numOfCurrentlyMet的记录也要变化. 变化了之后howManyToGo 也可能相应变化 (比如howManyToGo += 1).
如果howManyToGo一直是0, 那么head就可以放心地一直右移, 也就是一直缩短子串的长度, 直到移动一个head之后, howManyToGo 不再是0为止.
如果howManyToGo不再是0, 说明head右走的操作导致T中有一个字符从子串中消失了, 那么tail就要去开拓新的领域去重新发现新的缺失的字符.
然后当再次找到所有的必须字符的时候, 就再次检查, 当前的子串的长度是不是更短了.
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

print(Solution().minWindow(
# "XDOYEZODEYXNZ","XYZ"
"aa", "aa"
))





