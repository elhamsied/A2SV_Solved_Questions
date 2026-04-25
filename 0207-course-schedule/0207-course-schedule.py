class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)]
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(node):
        
            if visited[node] == 1:
                return False
            elif visited[node] == 2:
                return True
            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited [node] = 2
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
               if not dfs(i):
                return False
        return True
