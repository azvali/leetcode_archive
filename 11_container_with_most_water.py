def maxArea(height):
    
    l,r = 0, len(height) - 1
    res = 0
    
    
    while l < r:
        cur = min(height[l], height[r]) * (r - l)
        
        res = max(res, cur)
    
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
            
    return res
