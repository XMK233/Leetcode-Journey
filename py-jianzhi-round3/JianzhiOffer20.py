'''
[剑指 Offer 20. 表示数值的字符串 - 力扣（LeetCode）](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof)

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

 
'''
'''
状态机. 
states数组存的, 就是状态. 合法的数字必然从状态0开始, 然后根据其开头字符的不同, 分别转入0, 1, 2, 4状态. 
然后进入这几种状态的任意一种后, 又有几种字符选择, 然后又是一波转换. 
最后退出的时候, 得在善终的几种状态中才行. 

人家设计得很好. 要深刻理解为什么人家要这么写. 
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank' # 开始的时候一定是状态1, 只能有4种开始字符. 除此之外非法.
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e' # 状态1之后肯定得是状态2.
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        p = 0                           # start with state 0
        for c in s:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's'     # sign
            elif c in "eE": t = 'e'     # e or E
            elif c in ". ": t = c       # dot, blank
            else: t = '?'               # unknown
            if t not in states[p]: return False
            p = states[p][t]
        ## 最后一个字符必须得在这几种状态下, 否则就不算善终.
        return p in (2, 3, 7, 8)

print(Solution().isNumber("+.  123"))


# 作者：jyd
# 链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 参悟一下参考答案, 最关键的东西在于: 设计一个好的状态机, 状态的转移全靠这个了.
## 至于程序的设计, 则非常忠实地还原了状态机. 没什么可说的.
## 这道题考的就是状态机.