def removeDuplicates(nums):
    
    
    if len(nums) <= 2:
        return len(nums)
    
    write, read = 2,2
    
    
    while read < len(nums):
        
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
            
        read += 1
        
    return write
    
