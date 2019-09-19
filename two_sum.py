class Solutions:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        dict = {} 
        for i, e in enumerate(nums): 
            if (target - nums[i]) not in dict:  
                dict[nums[i]] = i 
            else:
                return [dict[target - nums[i]], i]


