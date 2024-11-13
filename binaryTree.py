class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.value = key

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, key):
    if self.root is None:
      self.root = Node(key)

    else:
      self._insert(self.root, key)

  def _insert(self, root, key):
    if key < root.value:
      if root.left is None:
        root.left = Node(key) 
      else:
        self._insert(root.left, key)

    else:
      if root.right is None:
        root.right = Node(key)
      else:
        self._insert(root.right, key) 

  def in_order_traversal(self, root):
    if root:
      self.in_order_traversal(root.left)
      print(root.value, end='')

  def pre_order_traversal(self, root):
    if root:
      print(root.value, end= '')

self.pre_order_traversal(root.left)
self.pre_order_traveral(root.right) 

  def post_order_traversal(self, root):
    if root:
      self.post_order_traversal(root.left)
      self.post_order_traversal(root.right)
        print(root.value, end = '')

  def search(self, key):
    return self.search(self.root, key) 

  def _search(self, root, key):
    if root is None or root.value == key:
      return root
    if key < root.value:
      return self._search(root.left, key) 
    return self._search(root.right, key) 

  def delete_node(root, key):
    if root is None:
      return root 
    if key < root.val:
      root.left = delete_node(root.left, key)
    elif key > root.val:
      root.right = delete_node(root.right, key) 
    else:
      # node w/ one or no child
      if root.left is None:
        temp = root.right
        root = None
        return temp 
      elif root.right is None:
        temp = root.left 
        root = None
        return temp 
      # node w/ 2 children
      temp = min_value_node(root.right)
      root.val = temp.val
      root.right = delete_node(root.right, temp.val) 
    return root 


# Example usage
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(20)
bt.insert(3)
bt.insert(7)

print("In Order Traversal:")
bt.in_order_traveresal(bt.root)      # Output: 3 5 7 10 20 

print("\nPre-Order Traversal:")
bt.pre_order_traversal(bt.root)      # Output: 10 5 3 7 20 

print("\nPost-order Traversal:")
bt.post_order_traversal(bt.root)     # Output: 3 7 5 20 10 

print("\nSearch for 7:")
found_node = bt.search(7)
print(found_node.value if found_node else "Not found")    # Output: 7 
