class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper_function(nums[1 :]) , self.helper_function(nums[: -1]))

    

    def helper_function(self, nums):
        n = len(nums)
        prev_1 , prev_2 = 0 , 0
        for i in range(n):
            curr = max(prev_1  , prev_2 + nums[i])
            prev_1 , prev_2 = curr , prev_1
        return prev_1

