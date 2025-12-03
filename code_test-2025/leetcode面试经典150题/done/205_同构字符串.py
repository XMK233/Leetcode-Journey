# 205. 同构字符串
# 简单

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        判断两个字符串是否是同构的
        
        思路解析：
        1. 两个字符串必须长度相同，否则不是同构的
        2. 创建两个字典，分别记录s到t和t到s的映射关系
        3. 遍历两个字符串，对于每个位置i：
           - 如果s[i]已经在s_to_t映射中，检查它是否映射到t[i]
           - 如果t[i]已经在t_to_s映射中，检查它是否映射到s[i]
           - 如果映射不存在，则创建新的映射
        4. 如果在任何点发现映射不一致，返回False；否则返回True
        
        参数:
            s: str - 第一个字符串
            t: str - 第二个字符串
        
        返回:
            bool - 两个字符串是否同构
        """
        # 首先检查两个字符串的长度是否相同
        if len(s) != len(t):
            return False
        
        # 创建两个字典，分别存储s到t和t到s的映射
        s_to_t = {}
        t_to_s = {}
        
        # 遍历两个字符串的每个字符
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # 检查s到t的映射
            if char_s in s_to_t:
                # 如果s[i]已经映射到其他字符，不是同构的
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # 检查t到s的映射，确保不同字符不映射到同一个字符
                if char_t in t_to_s:
                    # 如果t[i]已经被其他字符映射，不是同构的
                    if t_to_s[char_t] != char_s:
                        return False
                # 创建新的映射
                s_to_t[char_s] = char_t
                t_to_s[char_t] = char_s
        
        # 遍历完成，没有发现不一致的映射
        return True

# 测试样例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1: 同构字符串
    # s = "egg", t = "add"
    # 映射关系: e->a, g->d
    s1 = "egg"
    t1 = "add"
    print(f"测试用例1: s='{s1}', t='{t1}'")
    print(f"结果: {solution.isIsomorphic(s1, t1)}")  # 应该输出True
    
    # 测试用例2: 非同构字符串
    # s = "foo", t = "bar"
    # f映射到b，但o需要同时映射到a和r，这是不允许的
    s2 = "foo"
    t2 = "bar"
    print(f"测试用例2: s='{s2}', t='{t2}'")
    print(f"结果: {solution.isIsomorphic(s2, t2)}")  # 应该输出False
    
    # 测试用例3: 同构字符串
    # s = "paper", t = "title"
    # 映射关系: p->t, a->i, p->t, e->l, r->e
    s3 = "paper"
    t3 = "title"
    print(f"测试用例3: s='{s3}', t='{t3}'")
    print(f"结果: {solution.isIsomorphic(s3, t3)}")  # 应该输出True
    
    # 测试用例4: 非同构字符串
    # s = "badc", t = "baba"
    # a映射到a，但d需要映射到b，而b已经映射到b，这会导致两个不同字符映射到同一个字符
    s4 = "badc"
    t4 = "baba"
    print(f"测试用例4: s='{s4}', t='{t4}'")
    print(f"结果: {solution.isIsomorphic(s4, t4)}")  # 应该输出False