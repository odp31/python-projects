# Sorting Algorithms in python 

# 1. Bubble Sort: repeatedly steps thru list, compares adjacent items and swaps them if in wrong order 

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j] 
  return arr
  
arr = [21, 432, 5, 2, 331, 44, 6]
print(bubble_sort(arr))

# 2. Selection Sort: Divides list into 2 parts: sorted @ beginning and unsorted part @ end; repeatedly selects smallest or largest from unsorted and moves it to sorted 

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr 
  
arr = [62, 63, 76, 42, 35]
print(selection_sort(arr)


# 3. Insertion Sort: builds final sorted array one item at a time; much less efficient on larger lists than quicksort, heaprsort or mergesort 

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i] 
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1 
    arr[j + 1] = key
  return arr 

arr = [12, 11, 13, 5, 6] 
print(insertion_sort(arr))


# 4. MergeSort: divide and conquer algorithm; divides list into halves, sorts them, and merges them back together 
def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2 
    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0 
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1 
      else:
        arr[k] = R[j]
        j += 1 
      k += 1 

    while i < len(L):
      arr[k] = L[i]
      i += 1 
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1 
      k += 1 

  return arr

arr = [39, 53, 43, 83, 20, 9]
print(merge_sort(arr))


# 5. QuickSort: divide and conquer algorithm; picks an element as a pivot and partitions array around the pivot 
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x > pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr)) 




