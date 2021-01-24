'''
[剑指 Offer 31. 栈的压入、弹出序列 - 力扣（LeetCode）](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof)

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

 

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1


示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。


 

提示：


	0 <= pushed.length == popped.length <= 1000
	0 <= pushed[i], popped[i] < 1000
	pushed 是 popped 的排列。


注意：本题与主站 946 题相同：https://leetcode-cn.com/problems/validate-stack-sequences/
'''
'''
我自己有一个思路. 就是哈, 有一个栈.

如果栈是空的,那么从压栈序列里面找一个给它压栈进去.
对比栈顶元素和出栈序列的下一个值:
    如果一样, 那么就消掉这个栈顶元素和出栈序列的值; 
    如果不一样, 那么就判断:
        压栈序列已空, 说明没有后续的元素压栈了, 那就GG了, 返回false.
        如果非空, 那就把下一个元素给它压栈. 
(然后就一直循环)
循环结束, 就意味着可以返回true了. 

'''
'''
## 具体的思路是，利用一个栈，来复盘压入和弹出的顺序。
## 参考了一下推荐思路，然后自己实现了。
## 实现的不太好。
'''
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        if len(pushed) == 0:
            return True
        ## 假定两个数组都非空
        pushIndex = 1
        popIndex = 0
        stack = []
        stack.append(pushed[0])
        while popIndex < len(popped):
            if stack[-1] != popped[popIndex]:
                if pushIndex >= len(pushed):
                    return False
                else:
                    stack.append(pushed[pushIndex])
                    pushIndex += 1
            else:
                popIndex += 1
                stack.pop(-1)
                if len(stack) == 0:
                    if pushIndex < len(pushed):
                        stack.append(pushed[pushIndex])
        return True

s = Solution()
print(s.validateStackSequences(pushed = [1,0], popped = [1, 0]))

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