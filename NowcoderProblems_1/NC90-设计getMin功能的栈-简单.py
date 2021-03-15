# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c623426af02d4c189f92f2a99647bd34?tpId=117&&tqId=37793&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
实现一个特殊功能的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
示例1
输入
复制
[[1,3],[1,2],[1,1],[3],[2],[3]]
返回值
复制
[1,2]
备注:
有三种操作种类，op1表示push，op2表示pop，op3表示getMin。你需要返回和op3出现次数一样多的数组，表示每次getMin的答案

1<=操作总数<=1000000
-1000000<=每个操作数<=1000000
数据保证没有不合法的操作

剑指offer30
'''


#
# return a array which include all ans for op3
# @param op int整型二维数组 operator
# @return int整型一维数组
#
class Solution:
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

    def getMinStack(self, op):
        # write code here
        res = []
        for o in op:
            if o[0] == 1:
                self.push(o[1])
            elif o[0] == 2:
                self.pop()
            else:
                res.append(self.min())
        return res
