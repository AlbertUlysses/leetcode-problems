class Solution:
    def majorityElement(self, nums: List[int]) -> int: #define a function 
        _set = set(nums) # use the set function to retrive a list of the unique numbers
        temp_count = 0 # create a temp counter and set to zero
        majority_count = 0 # create a majority_count 
        for i, e in enumerate(_set): # iterate through the set
            temp_count = nums.count(e) # set the temp count to the number e is in the list
            if temp > majority_count: # if temp is more than majority_count
                majority_count = temp #then it's the new majority count
                ans = e # set the answer to e
        return ans
