# Last updated: 12/6/2025, 8:54:11 PM
1class Solution:
2    def sortByReflection(self, nums: List[int]) -> List[int]:
3        def reflect(x):
4            b = bin(x)[2:]
5            return int(b[::-1], 2)
6
7        pairs = [(reflect(x), x) for x in nums]
8        pairs.sort()
9        return [x for i, x in pairs]
10