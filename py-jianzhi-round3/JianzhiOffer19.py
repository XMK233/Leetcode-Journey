'''
[剑指 Offer 19. 正则表达式匹配 - 力扣（LeetCode）](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof)

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。


示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。


示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。


示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。


示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false


	s 可能为空，且只包含从 a-z 的小写字母。
	p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。


注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/
'''
'''
动态规划. 

比较重要的一点是, 两个输入字符串, 哪一个放横坐标, 哪一个放纵坐标. 
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = '#' + s, '#' + p
        m, n = len(s), len(p)
        ## dp数组, 纵坐标是字符串, 横坐标是正则表达式哦.
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        for i in range(m):
            for j in range(1, n):
                ## 如果是第一行, 那么单独看待.
                if i == 0:
                    ## 如果在第2列(从第0列开始的哦)及其以后, 遇上不是星号的符号
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j - 2]
                ## 如果p[j]等于s[i]或者是万能符, 那就直接等同于左上角的那个结果
                elif p[j] in [s[i], '.']:
                    dp[i][j] = dp[i - 1][j - 1]
                ## 如果当前p[j]是星号, 那么就要分两种情况看待了.
                elif p[j] == '*':
                    ## 如果p[j - 1], 也就是星号前面一个字符跟s[i]是相同的, 那么就看
                    ## dp[i - 1][j]是什么值就好了. 为什么呢? 这就相当于, 用当前的正则表达式段去拟合放弃当前值的字符串.
                    #
                    ## 如果p[j - 1], 也就是星号前面一个字符跟s[i]是不同的, 那么就看
                    ## dp[i][j - 2]是什么值就好了. 其实这里还是相对更好理解的.
                    dp[i][j] = j > 1 and dp[i][j - 2] or p[j - 1] in [s[i], '.'] and dp[i - 1][j]
                ## 如果当前两个串的字符不一样, 或者不是万能符, 也不是星号, 那就只能GG了.
                else:
                    dp[i][j] = False
        return dp[-1][-1]

print(Solution().isMatch("aab", "c*a*b"))

# 作者：loick
# 链接：https: // leetcode - cn.com / problems / zheng - ze - biao - da - shi - pi - pei - lcof / solution / dong - tai - gui - hua - er - wei - shu - zu - by - loick /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 利用动归来做，很好的思路，多学习学习

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()