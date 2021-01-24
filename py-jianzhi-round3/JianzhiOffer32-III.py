'''
[剑指 Offer 32 - III. 从上到下打印二叉树 III - 力扣（LeetCode）](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof)

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7


返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]


 

提示：


	节点总数 <= 1000

'''

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
        order = "leftToRight"
        bidirectionalQueue = [root]
        resCurLevel = []
        lastNodeOfThisLevel = bidirectionalQueue[-1] #root
        while len(bidirectionalQueue) != 0:
            if order == "leftToRight":
                ## 从左边吐出
                _ = bidirectionalQueue.pop(0)
                resCurLevel.append(_.val)
                ## 然后, 把刚吐出的节点的左,右节点往bidirectionalQueue的右边怼进去
                if _.left != None:
                    bidirectionalQueue.append(_.left)
                if _.right != None:
                    bidirectionalQueue.append(_.right)
                ## 如果这个时候, 当前层遍历到了最后一个节点了, 就要进入下一层\换方向\填充res数组之类的一系列操作了.
                if _ == lastNodeOfThisLevel:
                    order = "rightToLeft"
                    res.append(resCurLevel)
                    resCurLevel = []
                    if len(bidirectionalQueue) != 0:
                        ## 当前层遍历完之后, bidirectionalQueue里面就全部是下一层的点了, 所以下一层的最后一个吐出的节点将会是左边第一个点
                        lastNodeOfThisLevel = bidirectionalQueue[0]
            else:
                ## 从右边吐出
                _ = bidirectionalQueue.pop(-1)
                resCurLevel.append(_.val)
                ## 把刚吐出的节点的右节点, 左节点从左边怼进去.
                if _.right != None:
                    bidirectionalQueue.insert(0, _.right)
                if _.left != None:
                    bidirectionalQueue.insert(0, _.left)
                ## 然后看看要不要进入下一层
                if _ == lastNodeOfThisLevel:
                    order = "leftToRight"
                    res.append(resCurLevel)
                    resCurLevel = []
                    if len(bidirectionalQueue) != 0:
                        ## 当前层遍历完之后, bidirectionalQueue里面就全部是下一层的点了, 所以下一层的最后一个吐出的节点就是右边第一个点
                        lastNodeOfThisLevel = bidirectionalQueue[-1]

        return res

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

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()