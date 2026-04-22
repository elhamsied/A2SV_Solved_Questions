class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True 
            for nbr in graph[node]:
                if nbr not in visited:
                    stack.append(nbr)
                    visited.add(nbr)
        return False
