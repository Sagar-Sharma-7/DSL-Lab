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
            return ("found at %s"%mid)
        elif(l[mid] < k):
            count+=1
            s = mid + 1
        elif(l[mid] > k):
            count+=1
            e = mid- 1

    print("total comparision %d"%count)
    return("not found!")

def sentinel_search(arr, target):
    n = len(arr)
    last = arr[n - 1]
    arr[n - 1] = target

    i = 0
    while arr[i] != target:
        i += 1

    arr[n - 1] = last

    if i < n - 1 or arr[n - 1] == target:
        return True
    else:
        return False

def fibonacci_search(arr, target):
    count = 0
    
    n = len(arr)
    
    m2 = 0
    m1 = 1
    m0 = m2 + m1
    
    while m0 < n:
        m2 = m1
        m1 = m0
        m0 = m1 + m2
    
    offset = 0
    
    while m0 > 1:
        count+=1
        i = min(offset + m2, n - 1)
        
        if arr[i] < target:
            m0 = m1
            m1 = m2
            m2 = m0 - m1
            offset = i
        
        elif arr[i] > target:
            m0 = m2
            m1 = m1 - m2
            m2 = m0 - m1
        
        else:
            print("Total comparison: ", count)
            return True
        
    print("Total comparison: ", count)
    if m1 and offset < n - 1 and arr[offset + 1] == target:
        return True
    
    return False

# n = int(input("Enter number elements in list (in order): "))
# l = list();
# for i in range(n):
#     l.append(int(input("Enter element %d: "%i)))
l = eval(input("Enter your ordered list: "))
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

print()
print('\033[94m' + "\tSenital Search: " + '\033[0m')
starttime3 = datetime.now()
print(sentinel_search(l, k))
endtime3 = datetime.now()
print((endtime3.timestamp() * 1000 - starttime3.timestamp() * 1000), " ms")

print()
print('\033[94m' + "\tFibonacci Search: " + '\033[0m')
starttime4 = datetime.now()
print(fibonacci_search(l, k))
endtime4 = datetime.now()
print((endtime4.timestamp() * 1000 - starttime4.timestamp() * 1000), " ms")
