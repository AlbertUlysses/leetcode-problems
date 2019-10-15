class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for e in nums:
            ans = ans^e
        return ans

"""Runtime: 96 ms, faster than 88.85% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 6.56% of Python3 online submissions for Single Number."""
