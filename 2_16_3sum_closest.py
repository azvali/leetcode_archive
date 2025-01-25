def threeSumClosest(nums: list[int], target: int) -> int:
    
    
    res = float('inf')
    maxdiff = float('inf')
    nums.sort()
    
    for x in range(len(nums) - 2):
        
        l , r = x + 1, len(nums) - 1
        
        while l < r:
            cur = nums[x] + nums[l] + nums[r]
            
            curdiff = abs(cur - target)
            
            if curdiff < maxdiff:
                maxdiff = curdiff
                res = cur
                
            if cur < target:
                l += 1
                
            elif cur > target:
                r -= 1
            
            else:
                return cur
            
                
    return res
            