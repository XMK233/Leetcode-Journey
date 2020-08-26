import collections

class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False

root = Node()
current = root
for w in "apple":
    current = current.children[w] ## 如果有w这个key的话, 就返回这个key对应的value; 如果没有这个key,就新增一个key.
current.isword = True

print("stop here")