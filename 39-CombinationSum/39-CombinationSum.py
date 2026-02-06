# Last updated: 2/5/2026, 9:27:21 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        
4        def mainFun(ind, candidates, target, ans, v):
5
6            if target==0:
7                ans.append(v[:])
8                return
9
10            if ind==len(candidates) or target < 0:
11                return
12
13            v.append(candidates[ind])
14            mainFun(ind, candidates, target-candidates[ind], ans, v)
15
16            v.pop()
17            mainFun(ind+1, candidates, target, ans, v)
18
19
20
21
22
23
24        ans = []
25        v = []
26        mainFun(0, candidates, target, ans, v)
27        return ans