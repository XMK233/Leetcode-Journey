# 读取并执行原文件中的代码
with open("12. 整数转罗马数字.py", "r", encoding="utf-8") as f:
    code = f.read()
    exec(code)

# 创建Solution实例
solution = Solution()

# 测试用例1：num = 3749
test1 = solution.intToRoman(3749)
expected1 = "MMMDCCXLIX"
print(f"Test 1: num = 3749, Output: '{test1}', Expected: '{expected1}', Result: {'Pass' if test1 == expected1 else 'Fail'}")

# 测试用例2：num = 58
test2 = solution.intToRoman(58)
expected2 = "LVIII"
print(f"Test 2: num = 58, Output: '{test2}', Expected: '{expected2}', Result: {'Pass' if test2 == expected2 else 'Fail'}")

# 测试用例3：num = 1994
test3 = solution.intToRoman(1994)
expected3 = "MCMXCIV"
print(f"Test 3: num = 1994, Output: '{test3}', Expected: '{expected3}', Result: {'Pass' if test3 == expected3 else 'Fail'}")

# 测试用例4：num = 1
test4 = solution.intToRoman(1)
expected4 = "I"
print(f"Test 4: num = 1, Output: '{test4}', Expected: '{expected4}', Result: {'Pass' if test4 == expected4 else 'Fail'}")

# 测试用例5：num = 3999
test5 = solution.intToRoman(3999)
expected5 = "MMMCMXCIX"
print(f"Test 5: num = 3999, Output: '{test5}', Expected: '{expected5}', Result: {'Pass' if test5 == expected5 else 'Fail'}")