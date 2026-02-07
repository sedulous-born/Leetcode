# Last updated: 2/7/2026, 12:01:51 AM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        
4        def mainFun(ind, s, digits, map, ans):
5            if ind == len(digits):
6                ans.append(s)
7                return 
8
9            ch = map[ord(digits[ind])-ord("0")]
10
11            for i in ch:
12                mainFun(ind+1, s+i, digits, map, ans)
13
14            
15            
16        map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
17        ans = []
18        s = ""
19        mainFun(0, s, digits, map, ans)
20        return ans
21