class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjst_list = collections.defaultdict(list)
        for x, y in edges:
            adjst_list[x].append(y)
            adjst_list[y].append(x)
        visted = set()
        def dfs(node):
            if node == destination:
                return True
            visted.add(node)
            for a in adjst_list[node]:
                if a not in visted and dfs(a):
                    return True
            return False
        return dfs(source)
       
        
            
        
        
        
        
    