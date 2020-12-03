import functools
class Solution:
    def minNumber(self, nums):
        # write code here
        if not nums:
            return ""
        arr = list(str(x) for x in nums)
        def f(a,b):
            if a+b<b+a:
                return -1
            else:
                return 1
        arr.sort(key=functools.cmp_to_key(f))
        return int("".join(arr))


# https://blog.csdn.net/mabozi08/article/details/88929407
## 这道题的精髓在于怎么比两个字符串的大小.
### 即: a, b两个字符串, 如果a+b > b+a, 那么a就大于b.
## 得到了字符串比较大小的方法, 就可以利用这种大小关系进行排序, 把小的放到前面就行了.
## 这里利用了一个内置的库, 对数组实行自定义排序.
### 目测, 只要函数f(a, b)满足, 如果a >= b 返回1, 否则返回-1就可以被使用.

s = Solution()
print(s.minNumber([2, 10]))