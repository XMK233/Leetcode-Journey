# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """


#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """


#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """


#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """

## https://blog.csdn.net/fuxuemingzhu/article/details/79388432
## 方法是很巧妙的.
## 另辟蹊径, 用hash来指向后续的节点.
## 利用了collections.default(). 这个东西以后要多用, 多练. 看上去真是个好东西.

class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)