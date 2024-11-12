# 1. Huffman Coding
# Uses variable length codes to represent characters with shorter codes assigned to more frequent characters 

import heapq
from collections import defaultdict

class Node:
  def __init__(self, freq, symbol, left=None, right=None):
    self.freq = freq 
    self.symbol = symbol
    self.left = left
    self.right = right
    self.huff = ''

  def __lt__(self, nxt):
    return self.freq < nxt. freq

def huffman_coding(data):
  frequency = defaultdict(int)
    for char in data:
      frequency[char] += 1 

    heap = [Node(freq, symbol) for symbol, freq in frequency.items()]
    heapq.heapify(heap) 

    while len(heap) > 1:
      left = heapq.heappop(heap)
      right = heapq.heappop(heap)
        left.huff = '0'
        right.huff = '1'
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(heap, newNode)

    huff_codes = {}
    def generate_codes(node, val = '')
      newVal = val + node.huff
      if node.left:
        generate_code(node.left, newVal)
      if node.right:
        generate_code(node.right, newVal)
      if not node.left and not node.right:
        huff_codes[node.symbol] = newval

      root = heapq.heappop(heap)
        generate_codes(root)
        return huff_codes

data = "hello huffman"
huff_codes = huffman_coding(data)
print(huff_codes) 


# 2. Run Length Encoding (RLE)
# compresses data by replacing sequences of same data value with a single value and a count 

def rle_encode(data):
  encoding = ''
  i = 0
  while i < len(data):
    count = 1
    while i + 1 < len(data) and data[i] == data[i + 1]:
      i += 1
      count += 1 
    encoding += data[i] + str(count)

    i += 1 
  return encoding 

data = "AAAABBBCCDAA"
encoded_data = rle_encode(data)
print(encoded_data)          # output should be: A4B3C2D1A2 



# 3. Lempel Ziv Welch (LZW)
# compresses data by replacing sequences of characters with single codes 

def lzw_compress(uncompressed):
  dict_size = 256
  dictionary = {chr(i):i for i in range(dict_size)}
  w = ""
  result = []

  for c in uncompressed:
    wc = w + c 
    if wc in dictionary: 
      w = wc 
    else:
      result.append(dictionary[w])
      dictionary[wc] = dict_size 

      dict_size += 1 
      w = c
  if w:
    result.append(dictionary[w])
      return result 

data = "TOBEORNOTTOB3EORTOBEORNOT"
compressed_data = lzw_compress(data)
print(compressed_data) 
