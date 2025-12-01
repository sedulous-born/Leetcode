# Last updated: 11/30/2025, 7:46:16 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        
4        def rec(i, nums):
5            if i==0:
6                return nums[0]
7
8            if i==1:
9                return max(nums[0], nums[1])
10
11            p2 = nums[0]
12            p1 = max(nums[0], nums[1])
13
14            for j in range(2, i+1):
15                pick = nums[j] + p2
16                not_pick = p1
17
18                curr = max(pick, not_pick)
19                p2 = p1
20                p1 = curr
21
22            return p1
23
24
25        return rec(len(nums)-1, nums)