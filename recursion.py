# recursion: programming technique where func calls itself directly or indirectly 
# often used to solve problems that can be broken down into smaller, self-similar subproblems 

# 1. Simple- factorial 
def factorial(n):
  if n == 0:
    return 1 
  else:
    return n * factorial(n - 1)
result = factorial(5)
print(result) #output = 120 

def fibonacci(n):
  if n <= 1:
    return n 
  else:
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
  print(fibonacci(i))

# 2. tower of Hanoi: objective is to move all disks from source rod to destination, following:
# only one disk can be moved at a time, a disk can only be moved if it is the uppermost disk on a stack, 
# and a disk can only be moved onto an empty rod or onto a rod whose upperomost disk is larger 

def tower_of_hanoi(n, source, destination, auxiliary):
  """ moves n disks from source peg to destination peg using auxiliary peg
  Args:
    n: numDisks
    source: name of source peg
    destination: name of destination peg 
    auxiliary: name of auxilary peg 
    """
  if n == 1:
    print(f"Move disk 1 from {source} to {destination}")
    return 
  tower_of_hanoi(n-1, source, auxiliary, destination)
  print(f"Move disk {n} from {source} to {destination}")
  tower_of_hanoi(n-1, auxiliary, destination, source)

# example usage
n = 3 
tower_of_hanoi(n, 'A', 'C', 'B')



# 3. n queens problem: classic backtracking problem where you need to place N chess queens on an N x N chessboard
# such that no two queens attack eachother 

def is_safe(board, row, col):
  # check this row on left side
  for i in range(col):
    if board[row][i] == 1:
      return False

  # check upper diagonal on left side
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  # check lower diagonal on left side 
  for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  return True 

def solve_n_queens_until(board, col):
  if col >= len(board):
    return True
  for i in range(len(board)):
    if is_safe(board, i, col):
      board[i][col] = 1
      if solve_n_queens_util(board, col + 1):
        return True
      board[i][col] = 0

def solve_n_queens(n):
  board = [[0] * n for i in range(n)]
  if not solve_n_queens_util(board, 0):
    print("Solution doesn't exist")
    return False
  print(board)
  return True 

# example usage
n = 4
solve_n_queens(n) 


# 4. reverse a string recursively 
def reverse_string(s):
  if len(s) <= 1:
    return s
  else:
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello")) # output = olleh

# 4. check if string is palindrome recurisvely 
def is_palindrome(s):
  if len(s) <= 1:
    return True
  else:
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("racecar")) # true
print(is_palindrome("hello")) # false 


# 5. generate permutations of a string 
def permutations(s):
  if len(s) == 0:
    return ['']
  perm_lis = []
  for char in s:
    remaining_chars = s.replace(char, '', 1)
    for p in permutations(remaining_chars):
      perm_list.append(char + p)
  return perm_list

print(permutations("abc")) # output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


# 6. binary search recursively 
def rec_BinSearch(arr, target, low, high):
  if low > high:
    return -1
  mid = (low + high) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] < target:
    return rec_BinSearch(arr, target, mid+1, high)
  else:
    return rec_BinSearch(arr, target, low, mid-1)

arr = [2, 3, 4, 10, 40]
target = 10
result = rec_BinSearch(arr, target, 0, len(arr) -1)
if result != -1:
  print("element is present at index", str(result))
else:
  print("element is not present in array") 

# 7. calculate power of a number recursively 
def power(base, exponent):
  if exponent == 0:
    return 1
  elif exponent % 2 == 0:
    return power(base * base, exponent // 2)
  else:
    return base * power(base, exponent - 1)

print(power(2,3))    # output = 8
print(power(5,4))    # output = 625
