# Last updated: 2/5/2026, 11:07:35 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        
4        def mainFun(ind, nums, ans, n, curr):
5            if ind == n:
6                ans.append(curr.copy())
7                return
8
9            curr.append(nums[ind])
10            mainFun(ind + 1, nums, ans, n, curr)
11            curr.pop()   
12
13            mainFun(ind + 1, nums, ans, n, curr)
14
15
16        ans = []
17        curr = []
18        mainFun(0, nums, ans, len(nums), curr)
19        return ans