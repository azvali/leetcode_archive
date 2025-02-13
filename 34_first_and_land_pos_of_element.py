def searchRange(self, nums: List[int], target: int) -> List[int]:
    

    l , r = 0 , len(nums) - 1
    
    
    while l <= r:
        cur = l + (r - l) // 2
        
        if nums[cur] > target:
            r = cur - 1
            continue
        elif nums[cur] < target:
            l = cur + 1
            continue
        else:
            l , r = cur , cur
            
            while l > 0 and nums[l - 1] == nums[l]:
                l -= 1
                
            while r < len(nums) - 1 and nums[r + 1] == nums[r]:
                r += 1
            
            return [l , r]
    
    return [-1, -1]

            