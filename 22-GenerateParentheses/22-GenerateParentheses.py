# Last updated: 2/2/2026, 8:46:01 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        def mainFun(ind, s, open1, close, ans, n):
4            if open1 > n:
5                return
6            if (ind == 2*n):
7                ans.append(s)
8                return 
9
10            mainFun(ind+1, s+"(", open1+1, close, ans, n)
11            if (close < open1):
12                mainFun(ind+1, s+")", open1, close+1, ans, n)
13
14        ans = []
15        s = ""
16        mainFun(0, s, 0, 0, ans, n)
17        return ans