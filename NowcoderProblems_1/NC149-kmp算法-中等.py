'''
https://www.nowcoder.com/practice/bb1615c381cc4237919d1aa448083bcc?tpId=117&tqId=37859&companyId=665&rp=1&ru=%2Fcompany%2Fhome%2Fcode%2F665&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

题目描述
给你一个非空模板串S，一个文本串T，问S在T中出现了多少次
示例1
输入
复制
"ababab","abababab"
返回值
复制
2
示例2
输入
复制
"abab","abacabab"
返回值
复制
1

这里的解法本质上是暴力解法. 没有用到KMP算法. 应当研究研究.
'''

class Solution:
    def kmp(self , S , T ):
        # write code here
        count = 0
        for i in range(len(T)):
            if T[i] == S[0]:
                if i+len(S)>len(T):
                    break
                if T[i:i+len(S)] == S:
                    count += 1
        return count