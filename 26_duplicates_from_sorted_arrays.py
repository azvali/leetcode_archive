def removeDuplicates(nums: list[int]) -> int:
    
    
    p1, p2 = 0, 1
    res = 1
    
    while p2 < len(nums):
        
        while p2 < len(nums) and nums[p2] == nums[p1]:
            p2 += 1
            
        if p2 < len(nums) and nums[p2] != nums[p1]:
            res += 1
            p1 += 1
            nums[p1] = nums[p2]
        
    return res