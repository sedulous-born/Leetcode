# Last updated: 1/26/2026, 11:48:12 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        curr = nums[0]
4        best = nums[0]
5
6        for i in nums[1:]:
7            curr = max(i, curr + i)
8            best = max(best, curr)
9
10        return best