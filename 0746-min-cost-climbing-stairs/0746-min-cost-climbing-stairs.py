class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_2 = prev_1 = 0
        for i in range(2 , len(cost) + 1):
            curr = min( prev_1 + cost[i - 1] , prev_2 + cost[i - 2])
            prev_2 = prev_1
            prev_1 = curr
        return prev_1

        