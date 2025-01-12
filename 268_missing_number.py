def missingNumber(nums: List[int]) -> int:
    
    
    
    nums.sort()
    
    
    for x in range(len(nums)):

        if x == 0:
            continue

        diff = nums[x] - nums[x - 1]

        if diff > 1:
            return nums[x - 1] + 1

    return len(nums)
        
        

