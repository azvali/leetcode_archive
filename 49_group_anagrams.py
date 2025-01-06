def groupAnagrams(strs):
    
    hashmap = {}
    
    for x in strs:
        arrKey = []
        sortedWord = x.sort()
        
        for c in x:
            cur = ord(c) - ord("a")
            arrKey.append(cur)
            
        if arrKey not in hashmap:
            hashmap[tuple(arrKey)] = [x]
        else:
            hashmap[tuple(arrKey)].append(x)
        
    return list(hashmap.values())
