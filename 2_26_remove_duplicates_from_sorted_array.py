def removeDuplicates(nums: list[int]) -> int:
    
    
    
    if not nums:
        return 0
    
    
    length = 1
    
    write, read = 1, 1
    
    while read < len(nums):
        
        if nums[read] == nums[write - 1]:
            read += 1
            continue
        else:
            nums[write] = nums[read] 
            length += 1
            write += 1
            read += 1
        
    return length
        
        
        
    