class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)

        for i, j in prerequisites:
            courseMap[i].append(j)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        visitList = [UNVISITED for i in range(numCourses)]
        res = []

        def dfs(course):
            if visitList[course] == VISITED:
                return True
            if visitList[course] == VISITING:
                return False
            
            visitList[course] = VISITING
            for nei in courseMap[course]:
                if not dfs(nei):
                    return False
            visitList[course] = VISITED
            res.append(course)
            return True
            
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res