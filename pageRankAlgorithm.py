import numpy as np 

def page_rank(M, num_iterations = 100, d = 0.85):    # d: damping factor: accounts for probability a user will continue clicking on links 
  N = M.shape[1]
  v = np.random.rand(N, 1)
  v = v / np.linalg.norm(v, 1)
  M_hat = (d * M + (1 - d) / N) 

  for _ in range(num_iterations):
    v = M_hat @ v 
  return v 

# Example Usage
M = np. array([0, 0, 1, 0],
              [1/3, 0, 0, 1/2], 
              [1/3, 1/2, 0, 0], 
              [1/3, 1/2, 0, 1/2]])
ranks = page_rank(M)
print(ranks) 
