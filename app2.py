"""
set A = students who play cricket
set B = students who play badminton
set C = students who play football
"""

# {intersection}
def intersection(a, b):
    c = []
    for x in a:
        if (x in b):
            c.append(x)
    return c

#{union}
def union(a,b):
    c = a
    for x in b:
        if(x not in c):
            c.append(x)
    return c

# {union} - {intersection}
def subtraction(a,b):
    result = []
    for y in a:
        if(y not in b):
            result.append(y)
    return result

n = int(input("Total number of students: "))
a = eval(input("Enter list of students who play cricket: "))
b = eval(input("Enter list of students who play badminton: "))
c = eval(input("Enter list of students who play football: "))
print("\n")
print("List of students who play both cricket and badminton: ",intersection(a,b))
print("List of students who play either cricket or badminton but no both: ",subtraction(a,b))
print("Number of students who play neither circket nor badminton: ",n- len(union(a,b)))
print("Number of students who play cricket & football but not badminton: ", len(subtraction(intersection(a,c), b)))
print("Number of studetns who do not play any game: ",n - len(union(union(a,b),c)))
print("List of studetns who play at least one game: ", union(union(a,b), c))
print("List of studetns who play all the game: ", intersection(intersection(a,b),c))
