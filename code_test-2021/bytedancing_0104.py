# coding=utf-8

# string = "I love China"
# print(" ".join([s[::-1] for s in string.split(" ")]))

import sys

## 这个代码还是有问题的. 需要去网上学习一下非递归怎么做遍历.

class TreeNode:
    val = 0
    left = None
    right = None
    def __init__(self, val):
        self.val = val

# str = input()
# print(str)
# print('Hello,World!')

def inOrder(node):
    ## null
    # if node == None:
    #    return
    # inOrder(node.left)
    # print(node) ###
    # inOrder(node.right)

    ### 根节点入栈，左节点入栈，遇到null就弹出
    ## 一旦弹出，将弹出节点的右节点放入栈。
    # if node == None:
    #     return True
    ###
    res = []
    stack = []
    stack.append(node)
    while len(stack) != 0:  ## attention, stack 不为空
        if stack[-1] == None:
            stack.pop(-1)
        ###
        if stack[-1].left != None:
            stack.append(stack[-1].left)
        else:
            # print(stack[-1])
            res.append(stack[-1].val)
            tmp = stack.pop(-1)
            stack.append(tmp.right)
    return res
    # minInt = res[0]
    # for i in res:
    #     if i < minInt:
    #         return False
    #     minInt = i
    # return True

def buildTreeFromList(listOfNums):
    ##
    listOfNodes = []
    for n in listOfNums:
        if n != None:
            listOfNodes.append(TreeNode(n))
        else:
            listOfNodes.append(None)
    ##
    for i, n in enumerate(listOfNodes):
        if n == None:
            continue
        if 2 * i + 1 >= len(listOfNodes):
            break
        n.left = listOfNodes[2 * i + 1]
        if 2 * i + 2 >= len(listOfNodes):
            break
        n.right = listOfNodes[2 * i + 2]
    return listOfNodes[0]

treeRoot = buildTreeFromList([1, 2, 3, 4, 5, 6, 7])
print(inOrder(treeRoot))