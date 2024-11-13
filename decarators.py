# Decarators: allow you to modify behavior of functions/classes without directly changing their source code 
# often used for tasks like logging, timing, authentication 

# basic structure: essentially a function that takes another function as input and returns a new function 

#1: retry decorator: used to automatically retry a function if it fails 
import time

def retry(retries=3, delay=1):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for attempt in range(retries):
        try:
          return func(*args, **kwargs)
        except Exception as e:
          print(f"Attempt {attempt + 1} failed: {e}")
          time.sleep(delay)
      raise
    return wrapper
  return decorator 

@retry(retries=5, delay=2)
def my_function():
  # Some potentially failing operation 
  raise Exception("something went wrong")

# rate limiting decorator: used to limit numTimes a func can be called w/in a time period 
import time 
from functools import wraps

def rate_limit(max_calls, period):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      wrapper.last_call = wrapper.last_call or 0
      if time.time() - wrapper.last_call < period:
        raise RuntimeError("Rate limit exceeded")
      wrapper.last_call = time.time()
      return func(*args, **kwargs)
    wrapper.last_call = 0
    return wrapper
  return decorator 

# 3 caching decorators: can be used to cache results of a function call, improving performance 
from functools import wraps 
def cache(func):
  cache_dict = {}

  @wraps(func)
  def wrapper(*args, **kwargs):
    key = str(args) + str(kwargs)
    if key not in cache_dict:
      cache_dict[key] = func(*args, **kwargs)
    return cache_dict[key]
  return wrapper 


