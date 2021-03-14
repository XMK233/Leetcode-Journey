# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=117&&tqId=37774&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA.append(node)

    def pop(self):
        # return xx
        if len(self.stackB) > 0:
            return self.stackB.pop(-1)
        elif len(self.stackA) > 0:
            while len(self.stackA) > 0:
                self.stackB.append(
                    self.stackA.pop(-1)
                )
            return self.stackB.pop(-1)
        return -1
