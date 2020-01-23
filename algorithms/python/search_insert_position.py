class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: 
            return 0
        if nums[-1] < target: 
            return len(nums)
        i = 0
        while(nums[i] <= target):
            if nums[i] == target:
                return i
            i += 1
        return i
"""
Runtime: 44 ms, faster than 99.96% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.6 MB, less than 91.04% of Python3 online submissions for Search Insert Position.
"""
