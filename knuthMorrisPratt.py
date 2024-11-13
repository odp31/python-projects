# string searching algorithm that efficiently finds occurrences of a pattern within a text 

def compute_lps_array(pattern):
  M = len(pattern)
  lps = [0] * M
  len = 0 
  i = 1
  while i < M:
    if pattern[i] == pattern[len]:
      len += 1
      lps[i] = len
      i += 1
    else:
      if len != 0:
        len = lps[len - 1]
      else:
        lps[i] = 0 
        i += 1
  return lps 


def KMPSearch(pat, txt):
  M = len(pat)
  N = len(txt)
  lps = compute_lps_array(pat)
  i = 0 
  j = 0
  while i < N:
    if pat[j] == txt[i]:
      i += 1
      j += 1
    if j == M:
      print("Found pattern at index " + str(i - j))
      j = lps[j - 1]
    elif i < N and pat[j] != txt[i]:
      if j!= 0:
        j = lps[j -1]
      else:
        i += 1 
