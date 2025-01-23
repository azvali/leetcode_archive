def removeDuplicates(nums: list[int]) -> int:
    
    
    
    write, read = 1, 1
    
    if len(nums) <= 1:
        return len(nums)
    
    
    while read < len(nums):
        if nums[read] == nums[write - 1]:
            read += 1
            continue
        
        nums[write] = nums[read]
        write += 1
        read += 1
        
    return write
    