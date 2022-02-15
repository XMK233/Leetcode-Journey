# coding=utf-8
import sys

# str = input()
# print(str)
# print('Hello,World!')

# with open ("download.bat", "w") as d:
#     d.write("call activate py1\n")
#     for i in range(1, 81):
#         d.write("you-get https://www.bilibili.com/video/BV1jt4y1D78C?p={}\n".format(i))
#     d.write("pause\n")

## 求
def maxDepth(node):
    ##
    if node == None:
        return 0
    ##
    if len(node.children) == 0:
        return 1
    elif len(node.children) > 0:
        maxChildDepth = -1
        for child in node.children:
            maxChildDepth = max(maxChildDepth, maxDepth(child))
            # if maxDepth > maxChildDepth:
            #    maxChild
        return maxChildDepth + 1
    else:
        return -1


def findMaxDiameter(node):
    ###
    if node == None:
        return 0, 0
    if len(node.children) == 0:
        return 1, 1
    ###
    candidates = []
    childDepths = []
    for child in node.children:
        childMaxDiameter, childMaxDepth = findMaxDiameter(child)
        candidates.append(childMaxDiameter)
        childDepths.append(childMaxDepth)
    for i in range(0, len(childDepths) - 1):
        for j in range(i + 1, len(childDepths)):
            candidates.append(childDepths[i] + childDepths[j] + 1)
    return max(candidates), max(childDepths) + 1


def findMaxSubPart(node):
    def findMaxBranch(node):
        if node == None:
            return 0
        if len(node.children) == 0:
            return node.val
        childMaxBranch = float("-Inf")  ## 最小数字
        for child in node.children:
            childMaxBranch = max(childMaxBranch, findMaxBranch(child))
        if childMaxBranch > 0:
            return node.val + childMaxBranch
        else:
            return node.val

    ##
    if node == None:
        return 0
    if len(node.children) == 0:
        return max(node.val, 0)
    candidates = []
    childMaxBranches = []
    for child in node.children:
        childMaxSubpart = findMaxSubPart(child)
        candidates.append(childMaxSubpart)
        ##
        childMaxBranch = findMaxBranch(child)
        childMaxBranches.append(childMaxBranch)
    for i in range(0, len(childMaxBranches) - 1):
        for j in range(i + 1, len(childMaxBranches)):
            candidates.append(childMaxBranches[i] + childMaxBranches[j] + node.val)
    return max(max(candidates), 0)



