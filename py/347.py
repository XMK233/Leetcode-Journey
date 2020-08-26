class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data, res = {}, []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        bucket = [[] for i in range(len(nums)+1)]
        for key in data:
            bucket[data[key]].append(key)
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]

## 用哈希和桶排序. https://blog.csdn.net/coder_orz/article/details/52075042
## 桶排序有一个有点就是排序的复杂度可以到O(n)