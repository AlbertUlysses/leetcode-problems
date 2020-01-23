class Solution:
    """Takes in an array and returns it without duplicates, returns """
    _len = 1 #set length to one
    if len(nums)==0: # create a condition to check if the list is empty
        return 0 # if it is empty return 0
    for i in range(1,len(nums)): #create a for loop the length of the list
        if nums[i] != nums[i-1]: #create a conditional to check if the nums
            nums[len_] = nums[i] # if they match, then set it to the first place
            _len += 1 #increment the length
    return _len #returns the length of unique numbers in the list
