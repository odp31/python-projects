# python class that demonstrates various string operations and manipulations

class StringShowcase:
  def __init__(self, string):
    self.string = string 

  def length(self):
    # returns length of string
    return len(self.string)

  def reverse(self):
    # reverses string
    return self.string[::-1]

  def uppercase(self):
    return self.string.upper()

  def lowercase(self):
    return self.string.lower()

  def capitalize(self):
    return self.string.capitalize()

  def title(self):
    return self.string.title()

  def count_substring(self, substring):
    return self.string.count(substring)

  def replace_substring(self, old_substring, new_substring):
    return self.string.replace(old_substring, new_substring)

# Example Usage
my_string = "hello, world!"
showcase = StringShowcase(my_string)

print("Length:", showcase.length())
print("Reversed:", showcase.reverse())
print("Uppercase:", showcase.uppercase())
print("Lowercase:", showcase.lowercase())
print("Capitalized:", showcase.capitalize())
print("Title Case:", showcase.title()0
print("Count of '1': ", showcase.count_substring('l'))
print("replaced 'hello' with 'hi':", showcase.replace_substring('hello', 'hi'))
