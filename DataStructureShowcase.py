class DataStructureShowcase:
  def __init__(self):
    # list (mutable, ordered)
    self.my_list = [1, 2, 3, 4, 5]
    # tuple (immutable, ordered)
    self.my_tuple = (10, 20, 30)
    # set (unordered, unique)
    self.my_set = {1, 2, 3, 3, 4}
    # dictionary (key-value pairs)
    self.my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

  def demonstrate_list(self):
    print("List:", self.my_list)
    self.my_list.append(6) # add an element 
    print("List after appending:", self.my_list)
    print("list element at index 2:", self.my_list[2])

  def demonstrate_tuple(self):
    print("Tuple:", self.my_tuple)
    # tuples are immutable so you can't modify them directly 

  def demonstrate_set(self):
    print("Set:", self.my_set)
    self.my_set.add(5)    # add a new element 
    print("set after adding:", self.my_set)

  def demonstrate_dict(self):
    print("Dictionary:", self.my_dict)
    print("name:", self.my_dict['name'])
    self.my_dict['occupation'] = 'Engineer' # add new key value pair 
    print("Dictionary after adding: ", self.my_dict)

if __name__ == "__main__":
  showcase = DataStructureShowcase()
  showcase.demonstrate_list()
  showcase.demonstrate_tuple()
  showcase.demonstrate_set()
  showcase.demonstrate_dict()

