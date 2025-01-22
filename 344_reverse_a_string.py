def reverseString(s):
    
    
    l, r = 0, len(s) - 1
    
    
    while l < r:
        
        s[l], s[r] = s[r], s[l]
        
        l += 1
        r -= 1
        
        
    