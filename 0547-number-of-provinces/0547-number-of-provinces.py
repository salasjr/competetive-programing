class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited[node] = True
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for node in range(n):
            if not visited[node]:
                dfs(node)
                provinces += 1

        return provinces

        