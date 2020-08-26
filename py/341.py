# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [ni for ni in reversed(nestedList)]  # 反序压入栈，使第一个元素在栈顶

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()  # 是整数的时候pop出栈

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:  # 栈不为空的时候执行下面程序
            top = self.stack[-1]  # 取栈顶
            if top.isInteger():  # 当栈顶是整数的时候
                return True  # 返回true，本题中就去执行next 的程序了
            top = self.stack.pop()  # 如果栈顶不是整数，而是列表类型的
            for ni in reversed(top.getList()):  # 又将列表里面元素反序压入栈
                self.stack.append(ni)

        return False
# https://blog.csdn.net/maymay_/article/details/80162847

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())