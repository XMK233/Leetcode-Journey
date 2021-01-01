# -*- coding:utf-8 -*-
class TwoStacks:
    def twoStacksSort(self, numbers):
        # write code here
        ## 先把原数组的栈顶拿出来, 命名为a
        ## 然后再对比新栈里面的栈顶b; 如果a>b, 就把b放进原栈, 然后接着看, 直到a<=b或b为空, 这时就把a放进新栈即可.
        ## 直到原栈为空, 算法停止.
        ## 最后颠倒数组, 再将数组返回.
        ## 因为根据我的算法, 实际上我得到的是小数字在前面的结果. 而题目要求的是大数字在前.
        newStack = []
        a = None
        while (len(numbers) != 0):
            if a == None:
                a = numbers.pop(0)
            ##
            if len(newStack) == 0 or a <= newStack[0]:
                newStack.insert(0, a)
                a = None
            else:
                b = newStack.pop(0)
                numbers.insert(0, b)
        newStack.reverse()
        return newStack

s = TwoStacks()
print(s.twoStacksSort([1, 4, 2, 3, 5]))