# Longest Common Subsequence (LCS)
# classic example of dynamic programming; invovles finding 2 longest subsequence common to two sequences 

def lcs(X, Y):
  m = len(X)
  N = len(Y)

  # Create 2D array to store lengths of LCS 
  L = [[0] * (n + 1) for _ in range(m+1)]

  # Build L[m+1][n+1] table in bottom up fashion 
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0:
        L[i][j] = 0 
      elif X[i - 1] == Y[j - 1]:
        L[i][j] = L[i - 1][j - 1] + 1
      else:
        L[i][j] = max(L[i-1][j], L[i][j-1])


  index = L[m][n]
  lcs = [""] * (index + 1)
  lcs[index] = ""

  # start from rightmost bottom most corner and store characters in LCS 
  i = m
  j = n 

  while i > 0 and j > 0:
    if X[i -1] == Y[j -1]:
      lcs[index - 1] = X[i - 1]
      i -= 1
      j -= 1 
      index -= 1 
    elif L[i - 1][j] > L[i][j-1]:
      i -= 1 
    else:
      j -= 1 

  return "".join(lcs)


# Example Usage
X = "AGGTAB"
Y = "GXTXAYB"
print("Longest Common Subsequence:", lcs(X, Y))
