#!/usr/bin/env python3

import unittest

def binary_search(l=[1,2,3,4,5], value=3, low=0, high=4):
    if high < low:
        raise ValueError
    mid = int((low + high) / 2)
    if l[mid] > value:
        return binary_search(l, value, low, mid-1)
    elif l[mid] < value:
        return binary_search(l, value, mid+1, high)
    else:
        return mid

class BinarySearchTest(unittest.TestCase):

    def test_find(self):
        l = [1,2,3,4,5]
        index = binary_search(l, 5, 0, len(l) - 1)
        self.assertEqual(index, 4)

    def test_not_found(self):
        l = [1,2,3,4,5]
        self.assertRaises(ValueError, binary_search, l, 6, 0, len(l) -  1)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
