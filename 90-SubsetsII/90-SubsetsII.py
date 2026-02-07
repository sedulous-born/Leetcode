# Last updated: 2/6/2026, 9:29:16 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        
4        def mainFun(ind, nums, ans, v):
5            if ind == len(nums):
6                ans.append(v[:])
7                return
8
9            v.append(nums[ind])
10            mainFun(ind+1, nums, ans, v)
11
12            v.pop()
13            for j in range(ind+1, len(nums)):
14                if nums[j]!=nums[ind]:
15                    mainFun(j, nums, ans, v)
16                    return 
17
18            mainFun(len(nums), nums, ans, v)
19
20
21        ans = []
22        v = []
23        nums.sort()
24        mainFun(0, nums, ans, v)
25        return ans