
def zeroMat(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    rowHasZero = []
    colHasZero = []
    firstRowZero = False
    firstColZero = False
    
    ####prepare for the first column and first row
    for i in range(m):
        if matrix[i][0] == 0:
            rowHasZero.append(i)
    for j in range(n):
        if matrix[0][j] == 0:
            colHasZero.append(j)
    if rowHasZero:
        firstColZero = True
    if colHasZero:
        firstRowZero = True        
    
    ####check the rest of matrix
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                rowHasZero.append(i)
                colHasZero.append(j)
    
    ####set zeros
    for i in range(len(rowHasZero)):
        for j in range(n):
            matrix[i][j] = 0
    for i in range(len(colHasZero)):
        for j in range(m):
            matrix[i][j] = 0
    #####set zeroes for the first column and the first row
    if firstRowZero:
        for j in range(n):
            matrix[0][j] = 0
    if firstColZero:
        for j in range(m):
            matrix[j][0] = 0
    
    return matrix
def main():
    
    matrix = [[1,2,3,4],[0,3,7,4],[1,2,0,5]]
    a = zeroMat(matrix)
    print(a)

if __name__ == '__main__':
    main()
