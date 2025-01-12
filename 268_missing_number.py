def missingNumber(nums: List[int]) -> int:
    
    
    
    nums.sort()
    
    
    for x in range(1, len(nums)):

        if nums[0] != 0:
            return 0

        diff = nums[x] - nums[x - 1]

        if diff > 1:
            return nums[x - 1] + 1

    return len(nums)
        
        

