# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/93aacb4a887b46d897b00823f30bfea1?tpId=117&&tqId=37805&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
一个缓存结构需要实现如下功能。
set(key, value)：将记录(key, value)插入该结构
get(key)：返回key对应的value值
但是缓存结构中最多放K条记录，如果新的第K+1条记录要加入，就需要根据策略删掉一条记录，然后才能把新记录加入。这个策略为：在缓存结构的K条记录中，哪一个key从进入缓存结构的时刻开始，被调用set或者get的次数最少，就删掉这个key的记录；
如果调用次数最少的key有多个，上次调用发生最早的key被删除
这就是LFU缓存替换算法。实现这个结构，K作为参数给出
[要求]
set和get方法的时间复杂度为O(1)

若opt=1，接下来两个整数x, y，表示set(x, y)
若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1

对于每个操作2，输出一个答案
示例1
输入
复制
[[1,1,1],[1,2,2],[1,3,2],[1,2,4],[1,3,5],[2,2],[1,4,4],[2,1]],3
返回值
复制
[4,-1]
说明
在执行"1 2 4"后，"1 1 1"被删除。因此第二次询问的答案为-1
备注:
1 \leq k \leq n \leq 10^51≤k≤n≤10
5

-2 \times 10^9 \leq x,y \leq 2 \times 10^9−2×10
9
 ≤x,y≤2×10
9

这道题不做了, 直接抄.
'''
import collections


class Solution:
    def LFU(self, operators, k):
        # write code here
        self.k = k
        self.size = 0
        # {key: [val, freq]}
        self.kv = {}
        # {freq: dict}
        self.freq = collections.defaultdict(lambda: collections.OrderedDict())
        self.minFreq = 0
        ret = []
        for operator in operators:
            if operator[0] == 1:
                self.set(operator[1], operator[2])
            else:
                ret.append(self.get(operator[1]))
        return ret

    def set(self, key, val):
        if key in self.kv:
            del self.freq[self.kv[key][1]][key]
            self.freq[self.kv[key][1] + 1][key] = None
            if (self.minFreq == self.kv[key][1]) and (not self.freq[self.kv[key][1]]):
                self.minFreq += 1
            self.kv[key][0] = val
            self.kv[key][1] += 1
        else:
            if self.size == self.k:
                delete = self.freq[self.minFreq].popitem(last=False)[0]
                del self.kv[delete]
                self.size -= 1
            self.kv[key] = [val, 1]
            self.freq[1][key] = None
            self.minFreq = 1
            self.size += 1

    def get(self, key):
        if key not in self.kv:
            return -1
        del self.freq[self.kv[key][1]][key]
        if self.minFreq == self.kv[key][1] and not self.freq[self.kv[key][1]]:
            self.minFreq += 1
        self.kv[key][1] += 1
        self.freq[self.kv[key][1]][key] = None
        return self.kv[key][0]


S = Solution()
while True:
    try:
        s = input()
        i = s.rindex(',')
        k = int(s[i + 1:])
        ops = [list(map(int, line.split(','))) for line in s[2:i - 2].split('],[')]

        res = S.LFU(ops, k)
        res = '[%s]' % ','.join(list(map(str, res)))
        print(res)
    except:
        break