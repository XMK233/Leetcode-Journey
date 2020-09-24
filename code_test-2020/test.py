print(min([1, 2, 3, -2]))

# print([1, 2, 3] == [1, 3, 2])

# dic = {
#     (1, 2): "1, 2"
# }
# print(dic[(1, 2)])


# import collections
#
# class Node(object):
#     def __init__(self):
#         self.children = collections.defaultdict(Node)
#         self.isword = False
#
# root = Node()
# current = root
# for w in "apple":
#     current = current.children[w] ## 如果有w这个key的话, 就返回这个key对应的value; 如果没有这个key,就新增一个key.
# current.isword = True
#
# print("stop here")

# numbers = [
#     3, 1, 0, 6, 94, 111, 42, 4, 10, 1, 2, 5, 2, 3, 99, 0
# ]
# numbers = [
#     (0, 0), (0, 0), (1, 1), (0, 0), (15, 52), (0, 0),
#     (2, 5), (1, 2), (3, 3), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
#     (3, 68), (1, 1)
#  ]
# for n in numbers:
#     # print(n, '[{:.1f}\\%]'.format(n / 383 * 100))
#     print(
#         n,
#         "{}[{}]({}[{}])".format(
#             n[0], '{:.1f}\\%'.format(n[0]/26 * 100), n[1], '{:.1f}\\%'.format(n[1]/132*100)
#         ) if n[0] else '[{:.1f}\\%]'.format(n[0]/26 * 100)
#     )

# import re
# print(re.search("\W", "%") != None)