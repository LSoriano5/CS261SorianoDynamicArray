# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Leonardo Soriano

import numpy as np

class DynamicArray:
    def __init__(self):
      self.data = np.empty(10, dtype = object) 
      self.size = 0
      self.capacity = 10
      self.next_index = 0
    
    def is_empty(self):
       return self.size == 0
    
    def __len__(self):
       return self.size
    
    def append(self,value):
       if self.size == len(self.data):
         self.data = np.resize(self.data, 2 * len(self.data))
       self.data[self.size] = value
       self.size += 1

       if self.size == 1:
          self.next_index = 1

    def __getitem__(self,index):
       if index < 0 or index >= self.size:
           raise IndexError
       return self.data[index]
       
    def next_index(self,value):
       self.next_index = value
       return self.next_index
    
    def clear(self):
       self.size = 0
       self.next_index = 0

    def pop(self):
       if self.size == 0:
           raise IndexError
       last_element = self.data[self.size - 1]
       self.size -= 1
       return last_element
    
    def delete(self, index):
       if not (0 <= index < self.size):
          raise IndexError
       
       for i in range(index, self.size - 1):
          self.data[i] = self.data[i+1]
          
       self.size -=1
       
    



