def setZeroes(matrix: list[list[int]]) -> None:
    
    rowlen = len(matrix)
    collen = len(matrix[0])
    
    rows = [False] * rowlen
    cols = [False] * collen
    
    
    
    for x in range(len(matrix)):
        
        for n in range(len(matrix[0])):
            
            if matrix[x][n] == 0:
                rows[x] = True
                cols[n] = True

    
    for x in range(rowlen):
        if rows[x] == True:
            rowzero(matrix, x)
    
    for x in range(collen):
        if cols[x] == True:
            colzero(matrix, x)
    
    
    def rowzero(arr, row):
        
        for x in range(len(arr[row])):
            arr[row][x] = 0
            
        
    def colzero(arr, col):
        for x in range(len(arr)):
            arr[x][col] = 0
            
                
            
