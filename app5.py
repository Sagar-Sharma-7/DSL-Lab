#linear and binary search
from datetime import datetime

def linearSearch(l, k):
    count = 0
    for i in range(0, len(l)):
        if(l[i] == k):
            count+=1
            print("total comparision %d"%count)
            return("found at %d"%i)
        count+=1
        
    print("total comparision %d"%count)
    return ("not found!")

def binarySearch(l, k):
    s = 0
    e = len(l) - 1
    count = 0
    while(s <= e):
        mid = s + (e - s)//2
        if(l[mid] == k):
            count+=1
            print("total comparision %d"%count)
            return ("found at %s"%i)
        elif(l[mid] < k):
            count+=1
            s = mid + 1
        elif(l[mid] > k):
            count+=1
            e = mid- 1

    print("total comparision %d"%count)
    return("not found!")


n = int(input("Enter number elements in list (in order): "))
l = list();
for i in range(n):
    l.append(int(input("Enter element %d: "%i)))
k = int(input("Element to search: "))

print()
print('\033[94m' + "\tLinear Search: " + '\033[0m')

starttime1 = datetime.now()
print(linearSearch(l, k))
endtime1 = datetime.now()
print((endtime1.timestamp() * 1000 - starttime1.timestamp() * 1000), " ms")

print()
print('\033[94m' + "\tBineary Search: " + '\033[0m')
starttime2 = datetime.now()
print(binarySearch(l, k))
endtime2 = datetime.now()
print((endtime2.timestamp() * 1000 - starttime2.timestamp() * 1000), " ms")

