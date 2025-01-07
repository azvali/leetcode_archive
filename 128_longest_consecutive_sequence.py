def longest_consecutive(nums: list[int]) -> int:
    hashset = set(nums)
    res = 0
    curseq = 0
    for r in hashset:
        
        if r - 1 not in hashset:
            curseq = 1
            while r + curseq in hashset:
                curseq += 1
            res = max(res, curseq)
            
    
    return res
            
