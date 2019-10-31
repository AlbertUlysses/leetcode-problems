class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

"""
Runtime: 40 ms, faster than 70.75% of Python3 online submissions for Remove Element.
Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Remove Element.
"""
