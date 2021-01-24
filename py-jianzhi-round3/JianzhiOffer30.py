'''
[剑指 Offer 30. 包含min函数的栈 - 力扣（LeetCode）](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof)

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.


 

提示：


	各函数的调用总次数不超过 20000 次


 

注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackGeneral = []
        self.stackMin = []

    def push(self, x: int) -> None:
        self.stackGeneral.append(x)
        if len(self.stackMin) == 0:
            self.stackMin.append(x)
        else:
            self.stackMin.append(min(x, self.stackMin[-1]))

    def pop(self) -> None:
        if len(self.stackGeneral) == 0:
            pass
        else:
            self.stackMin.pop(-1)
            self.stackGeneral.pop(-1)

    def top(self) -> int:
        return None if len(self.stackGeneral) == 0 else self.stackGeneral[-1]

    def min(self) -> int:
        return None if len(self.stackMin) == 0 else self.stackMin[-1]

### 思路非常简单，就是如果新加入一个数字，那么min数组也要对应增加一个当前最小值。

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

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