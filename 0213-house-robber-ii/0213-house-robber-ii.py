class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.max_profit(nums[ 1 : ]) , self.max_profit(nums[: - 1]))

    def max_profit(self , nums):
        
        prev_1 = prev_2 = 0
        for i in range(len(nums)):
            curr = max(prev_1 , prev_2 + nums[i])
            prev_2 = prev_1
            prev_1 = curr
        return prev_1

        