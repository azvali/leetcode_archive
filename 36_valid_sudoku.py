class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        setValidNums = {"1","2","3","4","5","6","7","8","9"}


        def checkrow(arr):     

            for x in range(9):
                hashset = set()
                counter = 0
                while counter < 9:
                    cur = arr[x][counter]
                    if cur in hashset and cur in setValidNums:
                        return False
                    else:
                        hashset.add(cur)

                    counter += 1
            
            return True

        def checkcol(arr):

            for x in range(9):
                hashset = set()
                counter = 0
                while counter < 9:
                    cur = arr[counter][x]
                    if cur in hashset and cur in setValidNums:
                        return False
                    else:
                        hashset.add(cur)

                    counter += 1
            
            return True
        
        def check3x3(arr):

            starts = [
                [0,0],[0,3],[0,6],
                [3,0],[3,3],[3,6],
                [6,0],[6,3],[6,6]
            ]

            for i , j in starts:
                hashset = set()
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        cur = arr[row][col]
                        if cur == ".":
                            continue
                        if cur in hashset and cur in setValidNums:
                            return False
                        hashset.add(cur)
            
            return True


        if checkrow(board) and checkcol(board) and check3x3(board):
        
            return True

        return False
            



