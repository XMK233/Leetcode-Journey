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

在一轮dfs里面, 我得看最长的两条半径并更新全局的最大直径, 但是每一轮dfs只返回从这个点出发的最长半径. 呵呵哒.
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
    def solve(self, n, edges, val):
        ## section1_start
        ## 这个section的作用是做dfs的递归.
        def dfs(cur: int, parent: int) -> int: ## 从这个cur节点出发, 不走回头路, 走出两条最长的不重复的路径, 然后将这两条路径的长度加起来得到的结果返回即可.
            ## cur就是当前的点, 然后parent是指它的父节点.
            nonlocal ans
            top = [0, 0] ## 这个非常精髓. 关键在于储存一个点往出的第一和第二长的两条边.
            for nxt in graph[cur]:
                if nxt == parent: ## 因为构建的图是双向的图, 所以nxt有可能为parent. 因为不走回头路的原则, 若是遇到此情况, 直接跳过.
                    continue
                d = dfs(nxt, cur) ## 这里开始就是常规套路.
                if d + edge_val[(cur, nxt)] > top[0]:
                    top[0] = d + edge_val[(cur, nxt)]
                    if top[0] > top[1]: ## 值得注意的是, 这里用了一点小小的技巧. 就是top存储当前遇到的最长的两个"半径", 不断更新这个状元榜眼列表.
                        top[0], top[1] = top[1], top[0]
            ans = max(ans, sum(top)) ## 用全局来记录最大直径. 最大直径其实是受到当前记录的两个最大半径的和的影响的.
            return max(top) ## 返回最大半径.
        ## section1_end
        ## section2_start
        graph = collections.defaultdict(list)
        edge_val = dict()
        ans = 0
        for (i, j), v in zip(edges, val):
            graph[i].append(j)
            graph[j].append(i)
            edge_val[(i, j)] = edge_val[(j, i)] = v
        ## section2_end
        ## section3_start
        dfs(0, -1) ## 这里的话, 我感觉初始的时候从树的任何点起始都没所谓. 只不过任何输入应该都包括0作为起点, 所以啊从0开始是最稳妥的. 你从3开始也行, 但是万一有一个输入的图最多就到节点2岂不是很尴尬?
        return ans
        ## section3_end


while True:
    try:
        x = input()
        n, edges, val = eval("[" + x + "]")
        print(Solution().solve(n, edges, val))
    except:
        break