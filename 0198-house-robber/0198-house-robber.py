class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev_1 , prev_2 = 0 , 0
        for i in range(n):
            curr = max(prev_1 , prev_2 + nums[i])
            prev_2 , prev_1  = prev_1 , curr
        return prev_1

        