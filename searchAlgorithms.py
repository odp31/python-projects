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


# 3. Interpolation Search 
# uses interpolation to guess position of target value; more efficient than binarySearch for uniformly distributed data 

def interpolation_search(arr, x):
  lo = 0
  hi = (len(arr) - 1)

  while lo <= hi and x >= arr[lo] and x <= arr[hi]:
    pos = lo + int(((x - arr[lo]) * (hi - lo)) / (arr[hi] - arr[lo]))
    if arr[pos] == x:
      return pos
    if arr[pos] < x:
      lo = pos + 1
    else:
      hi = pos - 1
  return - 1


# 4. Jump Search
# works faster than linear search for sorted arrays; skips blocks of elements instead of checking each element 1 by 1

def jump_search(arr, x, n):
  step = int(math.sqrt(n))
  prev = 0 

  while arr[min(step, n) -1] < x:
    prev = step
    step += int(math.sqrt(n))
    if prev >= n:
      return -1

  while arr[prev] < x:
    prev += 1 

  if arr[prev] == x:
    return prev
return -1 


# 5. Exponential Search 
# can be used on sorted arrays; works by repeatedly doubling the interval unit until the interval's upper
# bound is > target value 

def exponential_search(arr, x):
  n = len(arr)
  if arr[0] == x:
    return 0 

  i = 1
  while i < n and arr[i] <= x:
    i = i * 2

  return binary_search(arr, i // 2, min(i, n-1), x)

# 6. Ternary Search 
# similar to binary search but instead of dividing the search space into two halves it divides it into
# 3 parts 

def ternary_search(arr, x):
  l, r = 0, len(arr) - 1

  while l <= r:
    mid1 = l + (r - 1) // 3
    mid2 = r - (r - 1) // 3

    if arr[mid1] == x:
      return mid1
    if arr[mid2] == x:
      return mid2

    if x < arr[mid1]:
      r = mid1 - 1
    elif x > arr[mid2]:
      l = mid2 + 1
    else:
      l = mid1 + 1
      r = mid2 - 1
  return -1 
