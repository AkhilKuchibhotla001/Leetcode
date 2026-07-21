class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_1 , prev_2 = 0 , 0
        for i in range(len(nums)):
            curr = max(prev_1 , prev_2 + nums[i])
            prev_2 , prev_1 = prev_1 , curr
        return curr
        