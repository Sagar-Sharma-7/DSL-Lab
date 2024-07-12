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
    result = []
    row = len(a[0])
    for i in range(row):
        x = len(a)
        l = list()
        while(x > 0):
            l.append(0)
            x -= 1
        result.append(l)
    for x in range(len(a[0])):
        for y in range(len(a)):
            result[x][y] = a[y][x]
    return result
    

def sum(a, b):
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

def multiply(a,b):
    result = []
    for i in range(len(a)):
        l = []
        for x in range(len(b[0])):
            l.append(0)
        result.append(l)

    for x in range(len(a)):
        for y in range(len(b[0])):
            for z in range(len(a[0])):
                result[x][y] += a[x][z] * b[z][y]
    return result

def saddle(a):
    b = transpose(a)

    for x in range(len(a)):
        minimum = min(a[x])
        i = a[x].index(minimum)
        maximum = max(b[i])
        if(maximum == minimum):
            return((x+1,i+1))
        
    return "does not exist"


print("\tSelect any of the following operation: ")
print("1: Check for upper triangular")
print("2: Sum of diagonal")
print("3: Transpose")
print("4: Sum of 2 matrix")
print("5: Subtract 2 matrix")
print("6: Multiply 2 matrix")
print("7: Find saddle point")

cmd = int(input("Enter operation number: "))

if(cmd == 1):
    print(triangular(getMatrix()))
elif(cmd == 2):
    print(diagonal(getMatrix()))
elif(cmd == 3):
    print(transpose(getMatrix()))
elif(cmd == 4):
    print(sum(getMatrix(), getMatrix()))
elif(cmd == 5):
    print(subtract(getMatrix(), getMatrix()))
elif(cmd == 6):
    print(multiply(getMatrix(), getMatrix()))
elif(cmd == 7):
    print(saddle(getMatrix()))







    