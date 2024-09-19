from datetime import datetime
import random


#radix sort
def radix_sort_with_buckets(arr):
    if not arr:
        return arr
    
    max_num = max(arr)
    pos = 1
    while max_num // pos > 0:
        buckets = [[] for _ in range(10)]

        for number in arr:
            digit = (number // pos) % 10
            buckets[digit].append(number)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        
        pos *= 10

    return arr

def counting_sort(arr, pos):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store the count of occurrences of each digit
    for number in arr:
        index = (number // pos) % 10
        count[index] += 1
    
    # Change count[i] so that it contains the position of this digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // pos) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the output array to arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    
    max_num = max(arr)
    pos = 1
    
    # Perform counting sort for each digit position
    while max_num // pos > 0:
        counting_sort(arr, pos)
        pos *= 10

    return arr

def quick_sort(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot (we choose the middle element for simplicity)
    pivot = arr[len(arr) // 2]

    # Separate the array into 3 parts
    left = [x for x in arr if x < pivot]   # Elements less than the pivot
    middle = [x for x in arr if x == pivot] # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort the left and right parts, then combine them
    return quick_sort(left) + middle + quick_sort(right)


n = 10000
min_value = 0
max_value = 10000
l = [random.randint(min_value, max_value) for _ in range(n)]

print("Sorted list:")
starttime1 = datetime.now()

print()
print("BUCKET SORT")
print(radix_sort_with_buckets(l))
endtime1 = datetime.now()
print("\nTime taken:")
print((endtime1.timestamp() * 1000 - starttime1.timestamp() * 1000), " ms")
