def threeSumClosest(nums: list[int], target: int) -> int:
    
    nums.sort()
    maxdiff = float('inf')
    res = float('inf')
    
    for x in range(len(nums)):
        l, r = x + 1, len(nums) - 1
        
        while l < r:
            cur = nums[x] + nums[l] + nums[r]
            
            if cur == target:
                return cur
            
            curdiff = abs(target - cur)

            if curdiff < maxdiff:
                res = cur
                maxdiff = curdiff
            
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            
    return res 
        
        
        
        