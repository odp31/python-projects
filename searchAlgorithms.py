# 1. Linear Search

# simplest search algorithm; checks each element in list until finds target value
# time complexity: (O(n))

def linear_search(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i
  return -1

arr = [2, 3, 4, 10, 40]
x = 10
print(linear_search(arr, x))

# 2. Binary Search 
# more efficient than LS but requires list to be sorted; repeatedly divides search interval in half
# time complexity: O(\log n))

def binary_search(arr, x):
  low = 0
  high = len(arr) - 1 
  mid = 0

  while low <= high:
    mid = (high + low) // 2

    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1 
    else:
      return mid

  return - 1

arr = [2, 3, 4, 10, 40]
x = 10 
print(binary_search(arr, x))    # output: 3 
