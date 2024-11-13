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
