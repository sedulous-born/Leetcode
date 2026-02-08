# Last updated: 2/7/2026, 9:42:34 PM
1class Solution:
2    def mergeAdjacent(self, nums: List[int]) -> List[int]:
3
4        st = []
5
6        for i in nums:
7            st.append(i)
8
9            while len(st) >= 2 and st[-1]==st[-2]:
10                val = st.pop()
11                st[-1] += val
12
13        return st