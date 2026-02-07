# Last updated: 2/6/2026, 11:06:02 PM
1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        
4        def mainFun(ind, sumi, k, ans, v):
5            if sumi==0 and len(v)==k:
6                ans.append(v[:])
7                return
8
9            if sumi<0 or len(v) > k:
10                return
11
12            for j in range(ind, 10):
13                if j<= sumi:
14                    v.append(j)
15                    mainFun(j+1, sumi-j, k, ans, v)
16                    v.pop()
17
18            
19
20            
21
22
23        v = []
24        ans = []
25        mainFun(1, n, k, ans, v)
26        return ans
27