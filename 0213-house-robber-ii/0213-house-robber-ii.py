class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper_function(nums):
            prev_2 , prev_1 = 0 , 0
            for num in nums:
                curr = max(prev_1 , prev_2 + num)
                prev_2 = prev_1
                prev_1 = curr
            return prev_1
        return max(helper_function(nums[1 :]) , helper_function(nums[ :  -1]))

    

        