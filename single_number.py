class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums) - sum(nums))
     
    
"""Runtime: 96 ms, faster than 88.85% of Python3 online submissions for Single Number.
Memory Usage: 16.3 MB, less than 6.56% of Python3 online submissions for Single Number."""
