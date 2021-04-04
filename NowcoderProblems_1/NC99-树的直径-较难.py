# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/a77b4f3d84bf4a7891519ffee9376df3?tpId=117&&tqId=37824&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一棵树，求出这棵树的直径，即树上最远两点的距离。
包含n个结点，n-1条边的连通图称为树。
示例1的树如下图所示。其中4到5之间的路径最长，是树的直径，距离为5+2+4=11

示例1
输入
复制
6,[[0,1],[1,5],[1,2],[2,3],[2,4]],[3,4,2,1,5]
返回值
复制
11


'''

class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

#
# 树的直径
# @param n int整型 树的节点个数
# @param Tree_edge Interval类一维数组 树的边
# @param Edge_value int整型一维数组 边的权值
# @return int整型
#
import collections


class Solution:
    def solve(self, n: int, edges, val):
        def dfs(cur: int, parent: int) -> int:
            nonlocal ans
            top = [0, 0]
            for nxt in graph[cur]:
                if nxt != parent:
                    d = dfs(nxt, cur)
                    if d + edge_val[(cur, nxt)] > top[0]:
                        top[0] = d + edge_val[(cur, nxt)]
                        if top[0] > top[1]:
                            top[0], top[1] = top[1], top[0]
            ans = max(ans, sum(top))
            return max(top)

        graph = collections.defaultdict(list)
        edge_val = dict()
        ans = 0
        for (i, j), v in zip(edges, val):
            graph[i].append(j)
            graph[j].append(i)
            edge_val[(i, j)] = edge_val[(j, i)] = v

        dfs(0, -1)
        return ans


while True:
    try:
        x = input()
        n, edges, val = eval("[" + x + "]")
        print(Solution().solve(n, edges, val))
    except:
        break