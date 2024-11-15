
def permute(lst):
    if len(lst) == 1:
        return lst
    rst = []
    for i in range(len(lst)):
        new_lst = lst[0:i-1] + lst[i+1:] ## lst.remove???
        sub_permutes = permute(new_lst)
        for sp in sub_permutes:
            rst.append([lst[i]] + sp)
    return rst

print(
    permute([1,2, 3])
)





class Solution:
    def maxInWindows(self , num, size):
        '''
        我大概理解了。
        最基础的一点，是用双向队列，放num的序号而不是num的值进去。
        这样有一个好处，就是容易判断序号是不是“过时”了。
        具体的操作是：
        【1】在前size个num数组数字的时候，按序把最大数字的序号放到双向队列dp后面，并且不断删掉dp前面数字比这个数字小的序号。
        （具体就是，拿num[dp[-1]]这个数字跟当前位置的数字num[i]比大小，如果小于的话，就不断pop掉dp[-1]直到不满足条件为止）
        【1.1】然后无论如何都把i加到dp的末尾。
        【2】后面的num数组数字，就一个一个看。看到某个序号的时候，不断看dp[0]这个序号是否过时，过时就pop掉，dp[0]序号不过时为止。
        【3】然后照做1、1.1的操作就好了。
        一直到判断完num[-1]元素，就完事儿了。
        :param num:
        :param size:
        :return:
        '''
        res = []
         #窗口大于数组长度的时候，返回空
        if size <= len(num) and size != 0:
            from collections import deque
            #双向队列
            dq = deque()
            #先遍历一个窗口
            for i in range(size):
                #去掉比自己先进队列的小于自己的值
                while len(dq) != 0 and num[dq[-1]] < num[i]:
                     dq.pop()
                dq.append(i)
            #遍历后续数组元素
            for i in range(size, len(num)):
                res.append(num[dq[0]])
                while len(dq) != 0 and dq[0] < (i - size + 1):
                    #弹出窗口移走后的值
                    dq.popleft()
                #加入新的值前，去掉比自己先进队列的小于自己的值
                while len(dq) != 0 and num[dq[-1]] < num[i]:
                    dq.pop()
                dq.append(i)
            res.append(num[dq[0]])
        return res

s = Solution()
print(
    s.maxInWindows([2,3,4,2,6,2,5,1], 3)
)