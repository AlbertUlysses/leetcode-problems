class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(nums)
        for i,e in enumerate(nums):
            if e != ans:
                return ans
            ans += 1
        return ans
"""
Runtime: 184 ms, faster than 9.07% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 6.45% of Python3 online submissions for Missing Number.
"""
