def backspaceCompare(s: str, t: str) -> bool:
    
    
    
    p1 = len(s) - 1
    p2 = len(t) - 1
    
    while p1 >= 0 or p2 >= 0:
        
        count1 = 0
        while p1 >= 0:
            if s[p1] == '#':
                count1 += 1
                p1 -= 1
            elif count1 > 0:
                p1 -= 1
                count1 -= 1
            else:
                break
            
            
        count2 = 0
        while p2 >= 0:
            if t[p2] == '#':
                count2 += 1
                p2 -= 1
            elif count2 > 0:
                p2 -= 1
                count2 -= 1
            else:
                break
            
        if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
            return False
        
        
        p1 -= 1
        p2 -= 1
        
        
    if p1 < 0  and p2 < 0:
        return True
    
    return False
            
        
        
    
    
    