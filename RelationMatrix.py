class RelationMatrix:   
    def __init__(self, rows): #self only shows up in the declaration
        #todo
        self.rows = rows
    
    def getEntry(self, i, j):
        r = len(self.rows)
        c = len(self.rows[0])-1
        
        if (i < 0 or i > r or j < 0 or j > c):
            raise IndexError("List index out of range")
        return self.rows[i][j]

    def getRow(self, i):
        r = len(self.rows[0])-1
        
        if (i < 0 or i > r):
            raise IndexError("List index out of range")
        return self.rows[i]
    
    def getCol(self, j):
        c = len(self.rows[0])-1
        columns = list(zip(*self.rows))
        
        if (j < 0 or j > c):
            raise IndexError("List index out of range")
        return list(columns[j])
    
    def getDiag(self, k):
        r = len(self.rows)
        c = len(self.rows[0])
        if k >= 0:
            return list(self.rows[i][i+k] for i in range(min(r,c-k)))
        else:
            return list(self.rows[j-k][j] for j in range(min(r+k,c)))
        if k > c - 1 or k < 1 - r:
            raise IndexError("List index out of range")
    