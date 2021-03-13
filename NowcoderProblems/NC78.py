class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList1(self, pHead):
        # write code here
        if not pHead:
            return None
        root = None
        while pHead:
            pHead.next,root,pHead = root,pHead,pHead.next
        return root


    def ReverseList(self, pHead):
        ## 没用递归。就一般解法。
        ## when the chain is empty
        if not pHead:
            return None
        ##
        tmp = None
        next = pHead.next
        while True:
            pHead.next = tmp
            tmp = pHead
            pHead = next
            if pHead == None:
                return tmp
            else:
                next = pHead.next
