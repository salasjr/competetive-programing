class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjacency_list = [[] for _ in range(n)]
    
        for road in roads:
            city1, city2 = road
            adjacency_list[city1].append(city2)
            adjacency_list[city2].append(city1)

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(adjacency_list[i]) + len(adjacency_list[j])
                if j in adjacency_list[i] or i in adjacency_list[j]:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank
