# Last updated: 1/10/2026, 10:47:18 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        left = [1]
4        for i in range(1, len(nums)):
5            left.append(left[i-1]*nums[i-1])
6
7        right = [1]
8        for i in range(len(nums)-2, -1, -1):
9            right.append(right[-1] * nums[i+1])
10
11        right = right[::-1]
12        ans = []
13
14        for i in range(len(nums)):
15            ans.append(left[i]*right[i])
16
17        return ans