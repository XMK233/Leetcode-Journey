# -*- coding: utf-8 -*-

'''
[面试题 17.07. 婴儿名字 - 力扣（LeetCode）](https://leetcode-cn.com/problems/baby-names-lcci)

每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

在结果列表中，选择字典序最小的名字作为真实名字。

示例：

输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]

提示：


	names.length <= 100000

'''
'''
参考的方法有错. 看我们能不能给它改了. 
'''

from collections import defaultdict

class UnionFind(object):
    def __init__(self, names):
        self.parent = {}
        for name in names:
            self.parent[name] = name

    def union(self, a, b):
        ### 参考的解答, 如果a或者b是names里没有的字符, 那么直接return.
        ### 修正后, a或者b若是names原来没有的字符, 那么这两个if相当于是对初始化def __init__()的一个补充.
        if a not in self.parent:
            self.parent[a] = a
        if b not in self.parent:
            self.parent[b] = b

        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a < root_b:
            self.parent[root_b] = root_a
        else:
            self.parent[root_a] = root_b

    def find_root(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        leetcode17.07
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        # 频率map
        freq_map = defaultdict(int)
        for name_freq in names:
            name, freq_str = (part.strip().strip(')') for part in name_freq.split('('))
            freq_map[name] = int(freq_str)
        # 初始化并查集
        uf = UnionFind(freq_map.keys())
        # 并操作
        for pair_str in synonyms:
            a, b = (name.strip().strip(')').strip('(') for name in pair_str.split(','))
            uf.union(a, b)
        # 生成结果
        result = []
        res_map = defaultdict(int)
        for name, freq in freq_map.items():
            res_map[uf.find_root(name)] += freq
        for name, freq in res_map.items():
            result.append('{}({})'.format(name, freq))
        return result

print(
    Solution().trulyMostPopular(
        names= ["a(10)","c(13)"],#["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"],
        synonyms= ["(a,b)","(c,d)","(b,c)"]# ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
    )
)

# 作者：column
# 链接：https://leetcode-cn.com/problems/baby-names-lcci/solution/luo-ji-qing-xi-dian-bu-xiang-ma-by-column/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import collections
class Solution1:
    def trulyMostPopular(self, names, synonyms):
        names_dict = dict()  # 改名为cnt更好
        parent = {key: key for key in names_dict}
        for name in names:  # 这里可以再优化,我有些啰嗦了
            name_lst1 = name.split("(")
            name_lst2 = name_lst1[1].split(")")
            names_dict[name_lst1[0]] = int(name_lst2[0])
        parent = {key: key for key in names_dict}
        # 下面这步确定没必要么? 如果一个name再synonyms里有,但names里没有, 又恰好这个name是真是name呢???
        # print(names_dict)
        # for item in synonyms:
        #     name1,name2 = item.split(",")
        #     name1,name2 = name1[1:],name2[:-1]
        #     if name1 not in names_dict:
        #         names_dict[name1] = 0
        #     if name2 not in names_dict:
        #         names_dict[name2] = 0

        parent = {key: key for key in names_dict}

        def find_root(name):
            while parent[name] != name:
                name = parent[name]
            return name

        def union(name1, name2):  # 这里一开始做错了, 忘了把name替换为root了
            root1 = find_root(name1)
            root2 = find_root(name2)
            if root1 < root2:
                parent[root2] = root1
            else:
                parent[root1] = root2

        for item in synonyms:
            name1, name2 = item.split(",")
            name1, name2 = name1[1:], name2[:-1]
            if parent.get(name1) is None or parent.get(name2) is None: continue
            union(name1, name2)
        res = collections.defaultdict(int)
        # print(parent)
        for key, val in parent.items():
            res[find_root(val)] += names_dict[key]  # 这里一开始做错了, 没有加find_root,所以就只得到了parent的.
        print(res)
        return [key + '(' + str(val) + ')' for key, val in res.items()]

# ["a(10)","c(13)"]
# ["(a,b)","(c,d)","(b,c)"]



# 作者：kincaid-3
# 链接：https://leetcode-cn.com/problems/baby-names-lcci/solution/python3-bing-cha-ji-by-kincaid-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。