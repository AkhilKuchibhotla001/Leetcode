class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper_function(nums[1 : ]) , self.helper_function(nums[ : -1]))

    def helper_function(self , nums):
        prev_1 , prev_2 = 0 , 0 

        for i in range(len(nums)):
            curr = max(prev_1 , prev_2 + nums[i])
            prev_2 , prev_1 = prev_1 , curr
        return prev_1
        