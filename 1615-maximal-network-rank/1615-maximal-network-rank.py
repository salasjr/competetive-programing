class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjacency_matrix = [[0] * n for _ in range(n)]
        for road in roads:
            city1, city2 = road
            adjacency_matrix[city1][city2] = 1
            adjacency_matrix[city2][city1] = 1
        print(adjacency_matrix)
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = sum(adjacency_matrix[i]) + sum(adjacency_matrix[j]) - adjacency_matrix[i][j]
                max_rank = max(max_rank, rank)

        return max_rank
       
      
        
        
        
        
        