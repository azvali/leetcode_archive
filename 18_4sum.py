def fourSum(nums: list[int], target: int) -> list[list[int]]:
    
    
    nums.sort()
    res = []
    
    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x - 1]:
            continue
        
        for n in range(x + 1, len(nums)):
            if n > x + 1 and nums[n] == nums[n - 1]:
                continue
            
            l,r = n + 1, len(nums) - 1

            while l < r:
                
                cur = nums[x] + nums[n] + nums[l] + nums[r]
                
                if cur > target:
                    r -= 1
                elif cur < target:
                    l += 1
                elif cur == target:
                    res.append([nums[x] , nums[n] , nums[l] , nums[r]])
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                        
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                    
    return res
