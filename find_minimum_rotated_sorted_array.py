class Solution:
    def findMin(self, nums: List[int]) -> int:
        _temp = nums[0]
        for i, e in enumerate(nums[1:]):
            if _temp > e:
                _temp = e
        return _temp


"""
Runtime: 44 ms, faster than 93.25% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.9 MB, less than 6.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
"""
