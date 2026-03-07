# Last updated: 3/6/2026, 8:26:46 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        h = {}
4        for i in range(len(nums)):
5            if (target - nums[i]) in h:
6                return [i, h[target-nums[i]]]
7            else:
8                h[nums[i]] = i
9
10        