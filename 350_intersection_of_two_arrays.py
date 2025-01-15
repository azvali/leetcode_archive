def intersect(nums1: list[int], nums2: list[int]) -> list[int]:


    res = []
    hashmap = {}
    
    for x in nums2:
        hashmap[x] = hashmap.get(x,0) + 1
            
    for x in nums1:
        
        if x in hashmap and hashmap[x] > 0:
            freq = hashmap.get(x, 0)
            
            res.append(x)
            hashmap[x] = hashmap.get(x, 0) - 1
            
        
    return res