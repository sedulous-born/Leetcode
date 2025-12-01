# Last updated: 11/30/2025, 8:41:10 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3
4        def houseRob(start, end, nums):
5
6            if start==end:
7                return nums[start]
8
9            p2 = nums[start]
10            p1 = max(nums[start], nums[start+1])
11
12            for i in range(start+2, end+1):
13                pick = nums[i] + p2
14                not_pick = p1
15                curr = max(pick, not_pick)
16                p2 = p1
17                p1 = curr
18
19            return p1
20
21        n = len(nums)
22        if n==0:
23            return 0
24        if n==1:
25            return nums[0]
26
27        first = houseRob(0, len(nums)-2, nums)
28        second = houseRob(1, len(nums)-1, nums)
29        return max(first, second)
30        