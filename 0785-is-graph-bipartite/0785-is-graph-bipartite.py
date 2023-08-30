class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set1=[0]*len(graph)
        
        def bfs(i):
            if set1[i]:
                return True
            q= deque([i])
            set1[i] = -1
            while q:
                i= q.popleft()
                for neighbor in graph[i]:
                    if set1[i] == set1[neighbor]:
                        return False
                    elif not set1[neighbor]:
                        q.append(neighbor)
                        set1[neighbor] = -1* set1[i]
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
                        
                        
                        
        
       
        
        