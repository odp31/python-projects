# Generators 
# only produce one value at a time, reducing memory usage, especially for large datasets 
# can be used to create infinite sequences

# 1. Generating Infinite Sequences 
def infinite_sequence():
  num = 0
  while True:
    yield num
    num += 1

# to use it:
gen = infinite_sequence()
for i in range(5):
  print(next(gen))

# 2. Reading files line by line
def read_file_line_by_line(filename):
  with open(filename, 'r') as f:
    for line in f:
      yield line.strip()

# to use it:
for line in read_file_line_by_line('my_file.txt'):
  print(line) 

# 3. Flattening Nested Lists
def flatten(nested_list):
  for item in nested_list:
    if isinstance(item, list):
      yield from flatten(item)
    else:
      yield item 
nested_list = [[1,2], 3, [4, 5, [6, 7]]]
for item in flatten(nested_list):
  print(item)

# 4. Implementing a custsom iterator 
class Coutndown:
  def __init__(self, start):
    self.start = start
  def __iter__(self):
    n = self.start
    while n > 0:
      yield n 
      n -= 1
# to use it 
for i in Countdown(5):
  print(i)

# 5. Permutations
def permutations(items):
  n = len(items)
  if n == 0:
    yield []
  else:
    for i in range(n):
      for perm in permutations(items[:i] + items[i+1:]):
        yield [items[i]] + perm 

# to use it:
for perm in permutations([1, 2, 3]):
  print(perm) 
