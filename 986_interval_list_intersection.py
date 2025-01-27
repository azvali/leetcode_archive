def intervalIntersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:


    if not firstList or not secondList:
        return []
    
    res = []

    i , j = 0, 0
    
    while i < len(firstList) and j < len(secondList):
        
        start1, finish1 = firstList[i][0], firstList[i][1]
        start2, finish2 = secondList[j][0], secondList[j][1]
        
        if start1 <= finish2 and start2 <= finish1:
            res.append([max(start1, start2), min(finish1, finish2)])
                   
        if finish1 < finish2:
            i += 1
        else:
            j += 1
            
    return res


