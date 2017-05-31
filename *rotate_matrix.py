
def rotateMat(mat):
    n = len(mat)
    i = 0
    
    while i < n / 2:
        for j in range(i, n - i - 1): ######important!!! n-1 you dont have to change the last element in the row
            temp = mat[i][j]
            mat[i][j] = mat[n - 1 -j][i]
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]
            mat[j][n - 1 - i] = temp
        i += 1
    return mat
        
def main():
    
    mat= [[1]]
    a = rotateMat(mat)
    print(a)

if __name__ == '__main__':
    main()
