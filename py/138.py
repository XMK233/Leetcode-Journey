# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


## https://cloud.tencent.com/developer/article/1406968
## 其实这种方法算是开挂了. 做一个旧点到新点地址的映射, 然后遍历一遍旧的链表, 一个一个把新链表给他接上.
## 比较酷炫的, 炫技的算法: https://blog.csdn.net/liuchonge/article/details/74858192
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        visited = dict()
        # 复制值
        node = head
        while node:
            visited[node] = Node(node.val)
            node = node.next

        # 给一个空值
        visited[None] = None

        # 复制关系
        node = head
        while node:
            visited[node].next = visited[node.next]
            visited[node].random = visited[node.random]
            node = node.next
        return visited[head]