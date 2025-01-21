def findDuplicate(nums: list[int]) -> int:
    
    nums.sort()
    
    for x in range(1, len(nums)):
                    
        if nums[x] == nums[x - 1]:
            return nums[x] 
        
        
        
        
# wrong answer use floyds algorithm
            