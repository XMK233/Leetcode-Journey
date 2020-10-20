class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

def buildChain(nums):
    nodes = [ListNode(num) for num in nums]
    for i, node in enumerate(nodes):
        if i == len(nums) - 1:
            node.next = None
        else:
            node.next = nodes[i + 1]
    return nodes[0]

def printChain(n):
    head = n
    while head != None:
        print(head.val)
        head = head.next
