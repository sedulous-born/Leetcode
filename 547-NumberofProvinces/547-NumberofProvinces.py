# Last updated: 3/24/2026, 11:35:03 AM
1from collections import deque
2class Solution:
3    def findCircleNum(self, isConnected: List[List[int]]) -> int:
4        def bfs(i, visited, adj, n):
5            queue = deque([i])
6            visited[i] = True
7            
8            while queue:
9                cur = queue.popleft()
10                for k in adj[cur]:
11                    if not visited[k]:
12                        queue.append(k)
13                        visited[k] = True
14                        
15            
16            
17        n = len(isConnected)
18        adj = [ [] for _ in range(n)]
19        for i in range(n):
20            for j in range(n):
21                if isConnected[i][j] and i!=j:
22                    adj[i].append(j)
23        count = 0
24        visited = [False] * n
25        for i in range(n):
26            if not visited[i]:
27                count+=1
28                bfs(i, visited, adj, n)
29            
30        return count