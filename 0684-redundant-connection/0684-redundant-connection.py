class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            while x != parent[x]:
                x = parent[x]

            return x

        for a , b in edges:

            parent_a = find(a)
            parent_b = find(b)

            if parent_a == parent_b:
                return [a , b]

            parent[parent_a] = parent_b






        