def missingNumber(nums: list[int]) -> int:
    
    
    
    nums.sort()
    
    if nums[0] != 0:
        return 0
        
        
    for x in range(1, len(nums)):

        diff = nums[x] - nums[x - 1]

        if diff > 1:
            return nums[x - 1] + 1

    return len(nums)
        
        

