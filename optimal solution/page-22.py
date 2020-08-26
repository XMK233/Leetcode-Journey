# -*- encoding=utf-8 -*-

class Node:
    value = -1
    left = None
    right = None

    def __init__(self, v):
        self.value = v


def getMaxTree(arr):  ## arr: [int, int, int,....]
    nArr = []
    for a in arr:
        nArr.append(Node(a))
    stack = []
    lBigMap = {}
    rBigMap = {}
    for curNode in nArr:
        while len(stack) != 0 and stack[-1].value < curNode.value:
            popStackSetMap(stack, lBigMap)
        stack.append(curNode)
    while len(stack) != 0:
        popStackSetMap(stack, lBigMap)
    for curNode in reversed(nArr):
        while len(stack) != 0 and stack[-1].value < curNode.value:
            popStackSetMap(stack, rBigMap)
        stack.append(curNode)
    while len(stack) != 0:
        popStackSetMap(stack, rBigMap)
    head = None
    for curNode in nArr:
        left = lBigMap.get(curNode)
        right = rBigMap.get(curNode)
        if left == None and right == None:
            head = curNode
        elif left == None:
            if right.left == None:
                right.left = curNode
            else:
                right.right = curNode
        elif right == None:
            if left.left == None:
                left.left = curNode
            else:
                left.right = curNode
        else:
            parent = left if left.value < right.value else right
            if parent.left == None:
                parent.left = curNode
            else:
                parent.right = curNode
    return head


def popStackSetMap(stack, a_map):
    popNode = stack.pop()
    if len(stack) == 0:
        a_map[popNode] = None
    else:
        a_map[popNode] = stack[-1]


h = getMaxTree([3, 4, 5, 1, 2])