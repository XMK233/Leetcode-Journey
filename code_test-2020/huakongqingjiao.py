class Node:
    val = None
    left = None
    right = None

    def __init__(self, v):
        self.val = v

class Solution:
    def restoreTree(self, l_pre, l_in):
        ### if the length of the list is 0:
        if len(l_pre) == 0:
            return None
        ### if the length of the list is only 1:
        if len(l_pre) == 1:
            return Node(l_pre[0])
        ### basic logic
        root = Node(l_pre[0])
        ##
        mid_index = l_in.index(l_pre[0])
        #
        l_in_left = l_in[0:mid_index]
        l_pre_left = l_pre[1:len(l_in_left) + 1]
        root.left = self.restoreTree(l_pre_left, l_in_left)
        #
        l_in_right = l_in[mid_index + 1:]
        l_pre_right = l_pre[len(l_in_left) + 1:]
        root.right = self.restoreTree(l_pre_right, l_in_right)
        return root


