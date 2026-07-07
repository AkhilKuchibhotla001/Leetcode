class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_1 , prev_2 = 0 , 0
        for num in nums:
            curr = max(prev_1 , prev_2 + num)
            prev_1 , prev_2 = curr , prev_1
        return prev_1
        