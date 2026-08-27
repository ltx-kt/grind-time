class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for i, j in prerequisites:
            courseMap[i].append(j)
        
        UNVISTED = 0
        VISTING = 1
        VISTED = 2

        visitList = [UNVISTED for i in  range(numCourses)]

        def dfs(num):
            if visitList[num] == VISTED:
                return True
            if visitList[num] == VISTING:
                return False

            visitList[num] = VISTING
            for nei in courseMap[num]:
                if not dfs(nei):
                    return False

            visitList[num] = VISTED
            return True


        for i in range(len(prerequisites)):
            if not dfs(prerequisites[i][0]):
                return False
        return True