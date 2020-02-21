class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid -1
            else:
                low = mid + 1
        return -1

"""
Runtime: 252 ms, faster than 94.64% of Python3 online submissions for Binary Search.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Binary Search.
"""
