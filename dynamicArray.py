import numpy as np
import time
import math
import sys
import os
import ctypes  # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array
        self.shrink_count = 0
        

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __str__(self):
        """Prints the numbers in the array"""
        S_list = [self._A[i] for i in range(self._n)]
        S_list.append(self.shrink_count)
        S_list.append(self._capacity)
        return " ".join(str(x) for x in S_list)

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _make_array(self, c):  # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value  # store newest element
        self._n += 1

    def shrink_array(self):
        """Shrink the Array size as required."""
        self.shrink_count += 1  # Do NOT modify this line

        # put your code here to shrink the array!
        self._resize(self._n)


    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item

                """
                As you can observe, the remove function does NOT shrink the 
                array size on removing an element. Your task is to implement 
                this code and make it space-efficient.
                """
                if (2*self._n==self._capacity):
                    # Replace True with your condition to call shring array
                    self.shrink_array()

                return  # exit immediately
        raise ValueError('value not found')  # only reached if no match

    def removeFromEnd(self, value):
        """Remove last occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n, 0, -1):
            if self._A[k-1] == value:  # found a match!
                for j in range(k-1, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item
                return  # exit immediately
        raise ValueError('value not found')  # only reached if no match








if __name__ == '__main__':
    a=DynamicArray()
    print(a.__str__())