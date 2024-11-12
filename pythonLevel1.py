def greet():
    print("Hello, World!")
greet()

# Function w/ return value 
def add_numbers(a,b):
    return a+b

result = add_numbers(5,3)
print(result) 

# Function w/ default argument 
def greet(name = "World"):
    print(f"Hello, {name}!")

greet()
greet("Alice")

# Function w/ Multiple Arguments 
def multiply(a, b):
  return a * b

result = multiply(4,5)
print(result) 

# Function w/ keyword arguments 
def describe_pet(animal_type, pet_name):
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name}.")

describe_pet(animal_type = 'hamster', pet_name = 'Harry')

# Function w/ Arbitrary Arguments 
def make_pizza(*toppings):
  print("\nMaking a pizza with the following toppings: ")
  for topping in toppings:
    print(f" - {topping})

make_pizza('pepperoni', 'mushrooms', 'extra cheese') 


