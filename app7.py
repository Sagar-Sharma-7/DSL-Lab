#sparse matrix
def addSparse(m1, m2):
    if(m1[0][0] == m2[0][0] and m1[0][1] == m2[0][1]):
        m = m1[0][0]
        n = m1[0][1]
        c1 = c2 = 1
        result = [[m, n, 0]]
        count = 0
        while(c1 < len(m1) and c2 < len(m2)):
            if(m1[c1][0] == m2[c2][0] and m1[c1][1] == m2[c2][1]):
                result.append([m1[c1][0], m2[c2][0], m1[c1][0] + m2[c2][0]])
                c1 +=1
                c2 +=1
                count += 1
            elif(m1[c1][0] == m2[c2][0]):
                if(m1[c1][1] < m2[c2][1]):
                    result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
                    c1 +=1
                    count +=1
                else:
                    result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
                    c2 +=1
                    count +=1
            else:
                if(m1[c1][0] < m2[c2][0]):
                    result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
                    c1 +=1
                    count +=1
                else:
                    result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
                    c2 +=1
                    count +=1
        
        while(c1 < len(m1)):
            result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
            c1 +=1
            count +=1
        while(c2 < len(m2)):
            result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
            c2 +=1
            count +=1

        result[0][2] = count
        print(result)

def getMatrix():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns:"))
    matrix = list();
    count = 0
    for i in range(m):
        for j in range(n):
            x = int(input("Enter element for a[%d][%d]: "%(i,j)))
            if(x != 0):
                matrix.append([i,j,x])
                count += 1

    return [[m,n,count]] + matrix;

def simpleTrans(mat):
    row = mat[0][1]  # Number of columns in the original matrix
    col = mat[0][0]  # Number of rows in the original matrix
    non_zero = mat[0][2]  # Number of non-zero elements

    # Initialize the transposed matrix with swapped dimensions
    transMat = [[row, col, non_zero]]

    # Prepare a list to hold transposed elements
    trans_elements = []

    # Transpose each non-zero element
    for i in range(1, non_zero + 1):
        r, c, v = mat[i]
        trans_elements.append([c, r, v])

    # Sort the transposed elements by row and column indices
    trans_elements.sort()

    # Append sorted transposed elements to the result matrix
    transMat.extend(trans_elements)

    return transMat

def fastTranspose(mat1):
    mat2 = [[mat1[0][1],mat1[0][0],mat1[0][2]]] + [0]* mat1[0][2]
    print(mat2)
    freq = [0] * (mat1[0][1]+1)
    for i in mat1[1:]:
        freq[(i[1])+1] += 1
    print(freq)
    freq[0]=1
    for i in range(1,len(freq)-1):
        freq[i] = freq[i-1]+freq[i]
    print (freq)
    print()

    
    for i in mat1[1:]:
        mat2[freq[i[1]]] = [i[1],i[0],i[2]]
        freq[i[1]]+=1
    for i in mat2:
        print(i)


while True:
    print("Menu:")
    print("1: Addition")
    print("2: Transpose")
    print("3: Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        print("Input matrix1")
        m1 = getMatrix()
        print(m1)
        
        print("Input matrix2")
        m2 = getMatrix()
        print(m2)
        addSparse(m1, m2)
    elif choice == '2':
        print("Input Matrix")
        m = getMatrix()
        print("Sparse matrix is: ")
        print(m)
        print(m)
        print("Simple Transpose is: ")
        fastTranspose(m)
    else:
        break


