class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i : [] for i in range(numCourses)}

        for crs , pre in prerequisites:
            hashmap[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if hashmap[crs] == []:
                return True

            visited.add(crs)

            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            hashmap[crs] = []
            visited.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True




        