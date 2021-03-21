# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/e96f1a44d4e44d9ab6289ee080099322?tpId=117&&tqId=37741&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
请实现支持'?'and'*'.的通配符模式匹配
'?' 可以匹配任何单个字符。
'*' 可以匹配任何字符序列（包括空序列）。
返回两个字符串是否匹配
函数声明为：
bool isMatch(const char *s, const char *p)
下面给出一些样例：
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "d*a*b") → false
示例1
输入
复制
"ab","?*"
返回值
复制
true

这道题跟前面做过的那个通配符的问题有一点不一样, 就是, 之前的题*表示的是若干个前面的字符, 而这里的*表示的是任意字符串.
这一点不同. 所以得用不同的方法来解.
'''
class Solution:
    def isMatch(self , s , p ):
        i=0
        j=0
        backi=-1
        backj=-1
        while(i<len(s)):
            if j<len(p) and (p[j] in [s[i], "?"]): ## 这里就很简单了, 只要碰到一样的字符, 直接后面的字符就好了.
                i=i+1
                j=j+1
            elif j<len(p) and p[j]=="*": ## 如果这个条件满足说明j是在*上的.
                backi=i
                backj=j ## 把backj指到*上
                j=j+1 ## j指到下一个去
            elif backj!=-1: ## 如果这个条件满足, 说明当前j没有指在*上, 但是backj在*上. ;;;如果这个条件不满足, 也就是backj == -1, 说明一直没有遇上过*, 然后s与p中又有不相同的字符, 直接GG.
                i=backi+1
                j=backj+1
                backi=i
            else:
                return False
        while (j<len(p) and p[j]=="*"): ## 应对的情况是, p最后有连续若干个*的情况. tnd, 我严重怀疑, 这种情况是不是作者一开始没ac, 后面找补回来的.
            j=j+1
        return j==len(p)

print(
    Solution().isMatch("ab", "?*")
)