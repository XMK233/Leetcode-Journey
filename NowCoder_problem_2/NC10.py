class Solution:
    def solve(self , s: str, t: str) -> str:
        # write code here
        sum_str = "0"
        if s == "0" or t == "0":
            return sum_str
        ls = len(s)
        lt = len(t)
        tot_res = []
        for i in range(ls-1, -1, -1): ## 倒着遍历s。其实做乘法的话，这里先遍历s还是t都无所谓。
            carry = 0
            res = ["0"] * (ls - i - 1) ## 结果数组
            v_s = s[i]
            for j in range(lt - 1, -1, -1): ## 倒着遍历t
                v_t = t[j]
                new_val = int(v_s) * int(v_t) + carry
                new_digit = new_val % 10
                carry = new_val // 10
                res.append(str(new_digit))
            if carry != 0:
                res.append(str(carry))

            sum_str = self.str_add(sum_str, "".join(res[::-1])) ## [::-1]这样反倒能更快？？？
        return sum_str

    def str_add(self, s: str, t: str) -> str:
        i, j = len(s) - 1, len(t) - 1        # 获取两个字符串长度
        add = 0                              # 标志进位
        ans = list()                         # 存储结果
        while i >= 0 or j >= 0 or add != 0:  # 判断两个字符串是否遍历完，并且是否仍需进位
            x = int(s[i]) if i >= 0 else 0   # 对s字符串取值或者无值后标记为0
            y = int(t[j]) if j >= 0 else 0   # 对t字符串取值或者无值后标记为0
            result = x + y + add             # 进行逐位加法
            ans.append(str(result % 10))     # 将余数作为一个加和后的数字存储在ans中
            add = result // 10               # 更新是否进位
            i -= 1
            j -= 1
        return "".join(ans[::-1])

print(
    Solution().solve("67892", "12345") == str(67892*12345)
)

'''
上面是我自己写的，怎么就超时了呢？
class Solution:
    def solve(self , s , t ):
        # write code here
        if s == "0" or t == "0":             # 特殊情况判断
            return "0"
         
        ans = "0"                            # 将乘法转换成子项的加法的累加阶段使用的变量
        m, n = len(s), len(t)                # 获得两段字符串的长度
        for i in range(n-1, -1, -1):         # 倒着遍历字符串t
            add = 0                          # 进位标识
            y = int(t[i])                    # 倒序取出字符串t的一个字符并转换成数字
            cur = ["0"] * (n - i - 1)        # 本轮次的补0个数
            for j in range(m-1, -1, -1):     # 倒着遍历字符串s
                x = int(s[j])                # 倒序取出字符串s的一个字符并转换成数字
                digit = x * y + add          # 两位相乘
                cur.append(str(digit % 10))  # 取出余数放在cur中
                add = digit // 10            # 标志是否进位
            if add > 0:                      # 判断是否最后仍需补位
                cur.append(str(add))
            cur = "".join(cur[::-1])         # 将cur中的元素倒序重新组成完整字符串
            ans = self.addStrings(ans, cur)  # 将乘法转换为加法的每一项调用addStrings进行字符串加和
        return ans                           # 返回最终结果
     
    def addStrings(self, s, t):              # 将两个字符串大数加和
        i, j = len(s) - 1, len(t) - 1        # 获取两个字符串长度
        add = 0                              # 标志进位
        ans = list()                         # 存储结果
        while i >= 0 or j >= 0 or add != 0:  # 判断两个字符串是否遍历完，并且是否仍需进位
            x = int(s[i]) if i >= 0 else 0   # 对s字符串取值或者无值后标记为0
            y = int(t[j]) if j >= 0 else 0   # 对t字符串取值或者无值后标记为0
            result = x + y + add             # 进行逐位加法
            ans.append(str(result % 10))     # 将余数作为一个加和后的数字存储在ans中
            add = result // 10               # 更新是否进位
            i -= 1
            j -= 1
        return "".join(ans[::-1])            # 最终倒序将数字重新组织成加和后的字符串
        
'''