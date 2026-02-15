# Last updated: 2/14/2026, 8:59:44 PM
1class Solution:
2    def firstUniqueFreq(self, nums: List[int]) -> int:
3        minaveloru = nums
4
5     
6        freq = Counter(minaveloru)
7        #20:1, 10:1, 30:2
8    
9
10        freq_count = Counter(freq.values())
11        #1:2 2:1
12        
13        for num in minaveloru:
14            if freq_count[freq[num]] == 1:
15                return num
16    
17        return -1