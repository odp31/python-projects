# Generator Functions: special type of function that returns an iterator 
# Use yield keyword to produce values one at a time (mem efficient for large datasets)

def fibonacci_generator(n):
  a, b = 0, 1
  for _ in range(n):
    yield a 
    a, b = b, a + b 

for num in fibonacci_generator(10):
  print(num) 

# iterating over files
with open('my_file.txt', 'r') as file:
  for line in file:
    print(line)

# iterating over dictionaries 
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
  print(key, value) 

# iterating over sets 
my_set = {1, 2, 3, 2, 1}
for item in my_set:
  print(item)

# custom iterators with __iter__ and __next__

class EvenNumbers:
  def __init__(self, max_value):
    self.max_value = max_value
    self.current = 0

  def __iter__(self):
    return self 

  def __next__(self):
    if self.current > self.max_value:
      raise StopIteration 
    num = self.current 
    self.current += 2 
    return num 

even_numbers = EvenNumbers(10)
for num in even_numbers:
  print(num)
  
