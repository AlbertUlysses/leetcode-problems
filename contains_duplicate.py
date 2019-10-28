class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


"""
Runtime: 132  ms, faster than 98.33% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19.2 MB, less than 16.98% of Python3 online submissions for Contains Duplicate.
"""
