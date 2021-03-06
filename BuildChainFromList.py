class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildChainFromList(l):
    nodes = [ListNode(i) for i in l]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

