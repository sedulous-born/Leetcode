# Last updated: 2/5/2026, 10:38:19 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        
4        def mainFun(ind, candidates, target, ans, v):
5            if target==0:
6                ans.append(v[:])
7                return 
8
9            if target<0 or ind==len(candidates):
10                return 
11
12            v.append(candidates[ind])
13            mainFun(ind+1, candidates, target - candidates[ind], ans, v)
14
15            v.pop()
16            for j in range(ind+1, len(candidates)):
17                if candidates[j] != candidates[ind]:
18                    mainFun(j, candidates, target, ans, v)
19                    break
20
21
22
23        ans = []
24        v = []
25        candidates.sort()
26        mainFun(0, candidates, target, ans, v)
27        return ans