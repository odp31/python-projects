class SetOperations:
  def __init__(self, set1, set2):
    self.set1 = set1
    self.set2 = set2

  def union(self):
    """ returns union of two sets """
    return self.set1.union(self.set2)

  def intersection(self):
    """ returns intersection of two sets """
    return self.set1.intersection(self.set2)

  def difference(self):
    """ returns difference of two sets (elements in set1 but not in set2) """
    return self.set1.difference(self.set2)

  def symmetric_difference(self):
    """ returns symmetric difference of two sets (elements in either set, but not both) """
    return self.set1.symmetric_difference(self.set2)

# Example Usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

operations = SetOperations(set1, set2)

print("Union:", operations.union())
print("Intersection:", operations.intersection())
print("Difference (set1 - set2):", operations.difference())
print("Symmetric Difference:", operations.symmetric_difference())

