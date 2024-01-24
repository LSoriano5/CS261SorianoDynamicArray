# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Leonardo Soriano

class DynamicArray:
    def __init__(self):
      self.data = []
      self.size = 0
      self.capacity = 10
    
    def is_empty(self):
       return self.size == 0

