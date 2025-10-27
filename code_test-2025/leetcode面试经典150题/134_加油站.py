# 134. 加油站
# 中等
# 134. 加油站
# 已解答
# 中等
# 相关标签
# premium lock icon
# 相关企业
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
# XMK：这个题这样做其实不是很好理解。但是就背住吧


from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        找出是否可以绕环路行驶一周的起点加油站，如果不存在则返回-1
        
        思路解析：
        1. 首先检查总油量是否小于总消耗，如果是，那么无论从哪里出发都不可能绕一圈
        2. 如果总油量大于等于总消耗，那么一定存在一个起点可以绕一圈
        3. 我们从索引0开始尝试，如果在某一点油箱变为负数，说明从起点到这一点的路径不可行
           将起点更新为下一个加油站，重新开始计算
        
        参数:
            gas: List[int] - 每个加油站可提供的汽油量
            cost: List[int] - 从每个加油站到下一个加油站的耗油量
        
        返回:
            int - 起始加油站的索引，如果无法绕一圈则返回-1
        """
        n = len(gas)
        
        # 计算总油量和总消耗
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # 如果总油量小于总消耗，无解
        if total_gas < total_cost:
            return -1
        
        # 当前剩余油量
        current_tank = 0
        # 起始加油站索引
        start_station = 0
        
        for i in range(n):
            # 在当前加油站加油并消耗到下一站的油
            current_tank += gas[i] - cost[i]
            
            # 如果当前油量为负，说明从start_station到i的路径不可行
            # 将起始点设为i+1，并重置油箱
            if current_tank < 0:
                start_station = i + 1
                current_tank = 0
        
        # 根据题目条件，如果存在解则保证唯一，所以返回start_station
        return start_station

# 测试样例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1: 可以环绕一周
    # 加油站信息: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    # 预期结果: 3
    # 解释: 从3号加油站出发，油量变化为: 4-1=3 → 3+5-2=6 → 6+1-3=4 → 4+2-4=2 → 2+3-5=0
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    print(f"测试用例1: gas={gas1}, cost={cost1}")
    print(f"结果: {solution.canCompleteCircuit(gas1, cost1)}")  # 应该输出3
    
    # 测试用例2: 不能环绕一周
    # 加油站信息: gas = [2,3,4], cost = [3,4,3]
    # 预期结果: -1
    # 解释: 总油量(9)小于总消耗(10)，无法环绕一周
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    print(f"测试用例2: gas={gas2}, cost={cost2}")
    print(f"结果: {solution.canCompleteCircuit(gas2, cost2)}")  # 应该输出-1