class Solution(object):
    def partition(self, s):
        def isPal(s):
            return s == s[::-1]
        ## 空串
        if s == "" or s == None:
            return [[]]
        ## 非空串, 就得好好处理了.
        res = []
        for i in range(len(s)):
            if isPal(s[:i+1]): ## 这个就是待测串,如果它是回文串,就递归dfs
                results = self.partition(s[i+1:])
                ## 对于每一个返回的result, 我们都给它加上s[:i+1]
                for result in results:
                    result.insert(0, s[:i+1])
                res.extend(results)
        return res

    def partition1(self, s):
        """
        https://blog.csdn.net/danspace1/article/details/88084384
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(len(s)):
                if isPal(s[:i + 1]):
                    dfs(s[i + 1:], path + [s[:i + 1]], res)
        def isPal(s):
            return s == s[::-1]
        res = []
        dfs(s, [], res)
        return res

s = Solution()
res = s.partition("aab")
print(res)

## https://blog.csdn.net/danspace1/article/details/88084384
## 思路, 看懂了上述代码后, 按照自己好理解的思路重写了一遍.
## 所以, 思路还是很重要. 你看, 你就不知道吧, 这道题怎么用dfs来做.
## 首先, "有多少种可能性"这种题目, 基本可以用回溯来做,
## 然后, 怎么实现回溯? 尝试用dfs.
## 为什么不是bfs? 因为bfs怎么有回溯嘛, 你说说看? 没有嘛....