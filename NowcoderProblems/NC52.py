'''
https://www.nowcoder.com/practice/37548e94a270412c8b9fb85643c8ccc2?tpId=117&tqId=37749&rp=1&ru=%2Fta%2Fjob-code-high&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

题目描述
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
示例1
输入
复制
"["
返回值
复制
false
示例2
输入
复制
"[]"
返回值
复制
true

'''

class Solution:
    def isValid(self , s ):
        # write code here
        stack = []
        for c in s:
            if c in "[{(":
                stack.append(c)
            elif c in "]})":
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == "(" and c == ")" or stack[-1] == "[" and c == "]" or stack[-1] == "{" and c == "}":
                        stack.pop(-1)
                    else:
                        return False
        if len(stack) > 0:
            return False
        return True
