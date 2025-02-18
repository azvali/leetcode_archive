def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
    l , r = 1 , max(piles)
    res = r

    while l <= r:
        cur = l + (r - l) // 2
        hours = 0

        for x in piles:
            hours += (x + cur - 1) // cur

        if hours <= h:
            res = cur
            r = cur - 1
        else:
            l = cur + 1

    return res
