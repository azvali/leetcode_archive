def isPalindrome(s: str) -> bool:
    
    
    s = s.lower()
    l , r = 0 , len(s) - 1
    
    
    while l < r:
        
        if not s[l].isalnum() and l < r:
            l += 1
            continue
    
        if not s[r].isalnum() and l < r:
            r -= 1
            continue
            
        
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    
    return True