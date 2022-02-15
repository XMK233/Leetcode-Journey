'''
描述
有一个有序数组A和一个整数val，请你用A构造一个结点值有序的无环单链表，并对其插入一个结点值为val的结点，并且保证这个无环单链表依然有序。

给定包含链表的所有元素的值（从头结点开始）的数组A，同时给定val，请构造出这个无环单链表，并返回插入该val值后的头结点。

数据范围：
0 < A.size() <= 1000
0 <= A中的元素值 <= 1000
0 < val <= 1000

例如当数组A为[1,3,4,5,7]，val为2时，插入val值后的链表变为{1,2,3,4,5,7}，

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A int整型一维数组
# @param val int整型
# @return ListNode类
#
class Solution:
    def insert(self , A, val):
        # write code here
        ## insert the val
        inserted_flag = False
        for i in range(len(A) - 1):
            if val < A[i]:
                A.insert(i, val)
                inserted_flag = True
                break
            elif val <= A[i + 1]:
                A.insert(i+1, val)
                inserted_flag = True
                break
        if not inserted_flag:
            A.append(val)
        ## create the chain
        ans = ListNode(-1)
        head = ans
        for v in A:
            ans.next = ListNode(v)
            ans = ans.next
        return head.next

s = Solution()