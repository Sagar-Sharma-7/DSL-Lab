#linear and binary search
from datetime import datetime

def linearSearch(l, k):
    for i in range(0, len(l)):
        if(l[i] == k):
            return("found at %d"%i)
    return ("not found!")

def binarySearch(l, k):
    s = 0
    e = len(l) - 1
    while(s <= e):
        mid = s + (e - s)//2
        if(l[mid] == k):
            return ("found at %s"%i)
        elif(l[mid] < k):
            s = mid + 1
        elif(l[mid] > k):
            e = mid- 1
    return("not found!")


n = int(input("Enter number elements in list (in order): "))
l = list();
for i in range(n):
    l.append(int(input("Enter element %d: "%i)))
k = int(input("Element to search: "))


starttime1 = datetime.now()
print(linearSearch(l, k))
endtime1 = datetime.now()
print((endtime1.timestamp() * 1000 - starttime1.timestamp() * 1000), " ms in linear search")

print()
starttime2 = datetime.now()
print(binarySearch(l, k))
endtime2 = datetime.now()
print((endtime2.timestamp() * 1000 - starttime2.timestamp() * 1000), " ms in binary search")

