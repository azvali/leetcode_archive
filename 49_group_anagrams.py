def groupAnagrams(strs):
    
    hashmap = {}
    
    for x in strs:
        arrKey = []
        sortedWord = x.sort()
        
        for c in sortedWord:
            cur = ord(c) - ord("a")
            arrKey.append(cur)
            
        if arrKey not in hashmap:
            hashmap[tuple(arrKey)] = [sortedWord]
        else:
            hashmap[tuple(arrKey)].append(sortedWord)
        
    return list(hashmap.values())
