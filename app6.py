#bubble sort
from datetime import datetime

def bubbleSort(l):
    swapped = False
    count = 0
    for x in range(len(l)):
        for i in range(0, len(l) - x - 1):
            count+=1
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
        if not swapped:
            break
    print(count)
    return l

def selectionSort(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1, len(l)):
            if(l[j] < l[i]):
                min = j
        l[i], l[min] = l[min], l[i]

    return l;

l = eval(input("Enter your unsorted list: "))
l2 = l.copy();
print("Sorted list:")
starttime1 = datetime.now()
print(bubbleSort(l))
endtime1 = datetime.now()
print("\nTime taken:")
print((endtime1.timestamp() * 1000 - starttime1.timestamp() * 1000), " ms")

print()
starttime2 = datetime.now()
print(selectionSort(l2))
endtime2 = datetime.now()
print("\nTime taken:")
print((endtime2.timestamp() * 1000 - starttime2.timestamp() * 1000), " ms")