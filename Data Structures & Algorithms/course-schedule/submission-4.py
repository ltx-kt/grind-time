class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = defaultdict(list)
        for k, v in prerequisites:
            hm[k].append(v)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        visit = [UNVISITED] * numCourses
        def dfs(c):
            if visit[c] == VISITING:
                return False
            if visit[c] == VISITED:
                return True
            visit[c] = VISITING

            for nei in hm[c]:
                if not dfs(nei):
                    return False
            visit[c] = VISITED
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True