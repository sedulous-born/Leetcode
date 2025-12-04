# Last updated: 12/3/2025, 10:25:54 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        ans = -1
4
5        for i in range(len(haystack)-len(needle)+1):
6            s = haystack[i:i+len(needle)]
7            if s==needle:
8                ans = i
9                break
10
11        return ans