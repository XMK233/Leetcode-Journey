class Solution:
    def sumNums(self, n: int) -> int:
        """
        python中的与（and）、或（or）、非（not）与java和c的不同之处在于
        A and B: 若A为False或其他空值（如：0, [], {}, ""等），则短路（不用再判断B是否为真，整个逻辑表达式已经为False了）
	    A or B:
        """
        return n and (n + self.sumNums(n-1))

## https://blog.csdn.net/besmarterbestronger/article/details/106480726
## 不用乘除，条件运算符之类的东西，那么就可以考虑利用递归来做了。
## 至于最后的返回类型，更是利用了python里面的技巧。
## 什么呢？
### 如果and的左边是1，那么返回and右边的值，而不一定是返回bool值。
### 如果or左边是0，那么直接返回or右边的值，而不一定是bool值。