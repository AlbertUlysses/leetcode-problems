class Solution:
    """Takes in an array and returns it without duplicates, returns """
    len_ = 1
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[len_] = nums[i]
            _len += 1
    return _len
