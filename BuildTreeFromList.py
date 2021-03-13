class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTreeFromList(l):
    l_node = []
    for _ in l:
        if _ == "#":
            l_node.append(None)
        else:
            l_node.append(TreeNode(_))
    i = 0
    while i < len(l_node):
        if l_node[i] == None:
            pass
        else:
            if i * 2 + 1 < len(l_node):
                l_node[i].left = l_node[i * 2 + 1]
            if i * 2 + 2 < len(l_node):
                l_node[i].right = l_node[i * 2 + 2]
        i += 1
    return l_node[0]