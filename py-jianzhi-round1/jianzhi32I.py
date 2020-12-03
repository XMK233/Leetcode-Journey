# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        ## 如果root为空:
        if root == None:
            return []
        ## 如果root是一个普通的数:
        res = []
        ### 初始化方向和当前层的最后一个节点:
        # order = "leftToRight"
        bidirectionalQueue = [root]
        resCurLevel = []
        # lastNodeOfThisLevel = bidirectionalQueue[-1] #root
        while len(bidirectionalQueue) != 0:
            # if order == "leftToRight":
            ## 从左边吐出
            _ = bidirectionalQueue.pop(0)
            resCurLevel.append(_.val)
            ## 然后, 把刚吐出的节点的左,右节点往bidirectionalQueue的右边怼进去
            if _.left != None:
                bidirectionalQueue.append(_.left)
            if _.right != None:
                bidirectionalQueue.append(_.right)
        return resCurLevel

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

treeRoot = buildTreeFromList([1, 2, 3, 4, 5, 6, None, 9, 10, None, None, 7, 8])
s = Solution()
print(s.levelOrder(treeRoot))
## 自己做出来的. 本质上还是按层打印树, 不一样的是呢, 要经常换方向, 要使用双端队列来辅助换方向.

