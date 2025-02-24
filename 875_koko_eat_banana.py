import math

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
    l , r = 1, max(piles)
    res = r
    
    while l <= r:
        mid = (l + r) // 2
        hours = 0
        
        for x in piles:
            hours += math.ceil(x / mid)
        
        if hours <= h:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return res
        
        