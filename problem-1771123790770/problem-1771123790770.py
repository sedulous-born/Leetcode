# Last updated: 2/14/2026, 8:49:50 PM
1class Solution:
2    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
3        l = []
4        for i in bulbs:
5            if i not in l:
6                l.append(i)
7            else:
8                l.remove(i)
9        return sorted(l)