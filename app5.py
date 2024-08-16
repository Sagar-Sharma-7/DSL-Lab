#bubble sort
from datetime import datetime

def bubbleSort(l):
    swapped = False
    count = 0
    for x in range(len(l)):
        for i in range(0, len(l) - x - 1):
            if l[i] > l[i+1]:
                count+=1
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
                print(l)
        if not swapped:
            break
    print("Total Comparisons: ", count)
    return l

def selectionSort(l):
    count1 = 0
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if(l[j] < l[min_index]):
                count1 += 1
                min_index = j
        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]
            print(l)
    
    print()
    print("Total comparisons: ", count1)
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
