class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, e in enumerate(nums):
            if e == 0:
                nums.remove(e)
                nums.append(e)

"""Runtime: 216 ms, faster than 9.61% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 5.97% of Python3 online submissions for Move Zeroes."""
