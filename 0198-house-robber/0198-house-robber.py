class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_2 , prev_1 = 0 , 0
        for num in nums:
            curr = max(prev_1 , prev_2 + num)
            prev_2 = prev_1
            prev_1 = curr
        return prev_1
        