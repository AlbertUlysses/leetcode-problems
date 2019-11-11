class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
                if temp > count:
                    count = temp
            else:
                temp = 0
        return count
"""
Runtime: 372 ms, faster than 99.26% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Max Consecutive Ones.
"""
