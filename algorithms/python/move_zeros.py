class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
# below is an answer that uses in place
def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[index], nums[i] = nums[i], nums[index]
                index +=1

