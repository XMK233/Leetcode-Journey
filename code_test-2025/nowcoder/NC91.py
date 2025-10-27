## NC91 最长上升子序列(三)

import bisect
class Solution:
    def LIS(self , arr ):
        # write code here
        n = len(arr)
        dp = [1] * n
        lenth = 1
        array = [arr[0]]
        for i in range(1, n):
            if arr[i] > array[-1]:
                lenth += 1
                dp[i] = lenth
                array.append(arr[i])
            else:
                index = bisect.bisect(array, arr[i]) ## 这个是节省时间的关键所在，一下能把本来n^2的变成nlogn了。
                dp[i] = index + 1
                array[index] = arr[i]
        res = []
        max_num = array[-1]
        max_num_index = arr.index(max_num)
        lenth = max(dp)
        for i in range(max_num_index, -1, -1):
            # if res == [] or arr[i] < res[-1]:
            #     res.append(arr[i])
            #     lenth -= 1
            #     if lenth == 0:
            #         break
            if res == [] or (arr[i] < res[-1] and dp[i] == lenth):
                res.append(arr[i])
                lenth -= 1
        return res[::-1]

print(
    Solution().LIS(
        [2,1,5,3,6,4,8,9,7]
    )
)