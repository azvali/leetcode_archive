def searchRange(nums: list[int], target: int) -> list[int]:
    
    
    def findleft(nums, k):
        l , r = 0 , len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] < k:
                l = mid + 1
            else:
                r = mid
                
        return l
    
    
    def findright(nums, k):
        l , r = 0 , len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > k:
                r = mid - 1
            else:
                l = mid
                
        return r
    
    
    
    l , r = findleft(nums, target), findright(nums, target)
    
    if l == r and nums[l] == target and nums[r] == target:
        return [l,r]
    else:
        return [-1,-1]
    
        