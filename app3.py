def getMatrix():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns:"))
    matrix = list();
    for i in range(m):
        x = [];
        for j in range(n):
            x.append(int(input("Enter element for a[%d][%d]: "%(i+1,j+1))));
        matrix.append(x);

    return matrix;

def triangular(a):
    print(a);
    for x in range(1, len(a)):
        for y in range(x):
            if(a[x][y] != 0):
                return False
    return True
                
def diagonal(a):
    sum = 0
    for x in range(len(a)):
        sum += a[x][x]
    return sum

def transpose(a):
    transposed = []
    # Loop through columns of the original matrix
    for i in range(len(matrix[0])):
        # Create a new row for the transposed matrix
        new_row = []
        # Loop through rows of the original matrix
        for j in range(len(matrix)):
            # Append the element from the original matrix to the new row
            new_row.append(matrix[j][i])
        # Add the new row to the transposed matrix
        transposed.append(new_row)
    return transposed
    

def sum_matrix(a, b):
    result = []
    for x in range(len(a)):
        row = []
        for y in range(len(a[0])):
            row.append(a[x][y] + b[x][y])
        result.append(row)
    return result

def subtract(a, b):
    result = []
    for x in range(len(a)):
        row = []
        for y in range(len(a[0])):
            row.append(a[x][y] - b[x][y])
        result.append(row)
    return result

def multiply(matrix1,matrix2):
   # Get the number of rows and columns for both matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if the matrices can be multiplied
    if cols_matrix1 != rows_matrix2:
        return "Matrices cannot be multiplied"

    # Create an empty result matrix with the correct size
    result = []
    
    # Loop through rows of matrix1
    for i in range(rows_matrix1):
        new_row = []
        # Loop through columns of matrix2
        for j in range(cols_matrix2):
            # Initialize the sum to calculate the dot product
            total = 0
            # Loop through the elements in the row of matrix1 and column of matrix2
            for k in range(cols_matrix1):
                total += matrix1[i][k] * matrix2[k][j]
            # Add the calculated total to the new row
            new_row.append(total)
        # Append the new row to the result matrix
        result.append(new_row)

    return result

def saddle(a):
    saddle_points = []
    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        row_min = a[i][0]
        min_col_i = [0]
        for j in range(1, cols):
            if a[i][j] < row_min:
                min_col_i = [j]
            elif a[i][j] == row_min:
                min_col_i.append(j)
        for col_i in min_col_i:
            is_saddle = True
            for k in range(rows):
                if a[k][col_i] > row_min:
                    is_saddle = False
                    break
            if is_saddle:
                saddle_points.append((i + 1, col_i + 1))

    return saddle_points
    # b = transpose(a)

    # for x in range(len(a)):
    #     minimum = min(a[x])
    #     i = a[x].index(minimum)
    #     maximum = max(b[i])
    #     if(maximum == minimum):
    #         return(((x+1,i+1), minimum))
        
    # return "does not exist"

def magicSq(a):
    n = len(a)
    common_sum = sum(a[0])
    for row in a:
        if sum(row) != common_sum:
            return False
        
    for col in range(n):
        col_sum = 0
        for row in range(n):
            col_sum += a[row][col]
        if col_sum != common_sum:
            return False
    
    first_diagonal_sum = 0
    for i in range(n):
        first_diagonal_sum += a[i][i]
    if first_diagonal_sum != common_sum:
        return False
    second_diagonal_sum = 0
    for i in range(n):
        second_diagonal_sum += a[i][n - i - 1]
    if second_diagonal_sum != common_sum:
        return False
    
    return True

print("\tSelect any of the following operation: ")
print("1: Check for upper triangular")
print("2: Sum of diagonal")
print("3: Transpose")
print("4: Sum of 2 matrix")
print("5: Subtract 2 matrix")
print("6: Multiply 2 matrix")
print("7: Find saddle point")
print("8: Check for magic square")

cmd = int(input("Enter operation number: "))

if(cmd == 1):
    print(triangular(getMatrix()))
elif(cmd == 2):
    print(diagonal(getMatrix()))
elif(cmd == 3):
    print(transpose(getMatrix()))
elif(cmd == 4):
    print(sum_matrix(getMatrix(), getMatrix()))
elif(cmd == 5):
    print(subtract(getMatrix(), getMatrix()))
elif(cmd == 6):
    print(multiply(getMatrix(), getMatrix()))
elif(cmd == 7):
    print(saddle(getMatrix()))
elif(cmd == 8):
    print(magicSq(getMatrix()))
else:
    print("invalid!")








    
