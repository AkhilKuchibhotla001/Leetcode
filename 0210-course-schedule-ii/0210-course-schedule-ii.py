class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = { i : [] for i in range(numCourses)}

        for crs , pre in prerequisites:
            hashmap[crs].append(pre)
        
        visiting = set()
        visited = set()

        output = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)

            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            visited.add(crs)

            output.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output


        


        