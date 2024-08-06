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

print("Input matrix1")
m1 = getMatrix()
print(m1)

print("Input matrix2")
m2 = getMatrix()
print(m2)

addSparse(m1, m2)


