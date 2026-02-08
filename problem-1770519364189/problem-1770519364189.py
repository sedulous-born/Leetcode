# Last updated: 2/7/2026, 8:56:04 PM
1class Solution:
2    def dominantIndices(self, nums: List[int]) -> int:
3
4        j = 1
5        avg = []
6        sumi = 0
7        for i in nums[::-1]:
8            sumi += i
9            avg.append(sumi/j)
10            j+=1
11
12        avg = avg[::-1]
13
14        count = 0
15        for i in range(len(nums)-1):
16            if nums[i] > avg[i+1]:
17                count += 1
18
19        return count
20            
21            
22        