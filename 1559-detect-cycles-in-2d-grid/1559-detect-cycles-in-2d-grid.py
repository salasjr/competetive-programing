class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j, parent_i, parent_j, color):
            if (i, j) in visited:
                return True

            visited.add((i, j))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < rows and 0 <= new_j < cols and (new_i != parent_i or new_j != parent_j) and grid[new_i][new_j] == grid[i][j]:
                    if dfs(new_i, new_j, i, j, color):
                        return True

            return False

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False