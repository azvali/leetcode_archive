def wordPattern(pattern: str, s: str) -> bool:
    
    hashmap = {}
    arr = []
    word = ""
    
    for x in s:
        if x != " ":
            word += x
            continue
        arr.append(word)
        word = ""
        
    if word:
        arr.append(word)
    
    # ^^^ the split() method would do what this does so it would be better to just do arr = s.split() and it would split the string into words
        
        
    if len(pattern) != len(arr):
        return False
    
    for i, j in zip(pattern, arr):
        if i not in hashmap:
            hashmap[i] = j
        else:
            if hashmap[i] != j:
                return False
        
    return True
            
    
    
            
            
            
        
            
           
