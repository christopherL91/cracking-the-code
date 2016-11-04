#!/usr/bin/env python3

import unittest

def unique(l):
    buf = [False] * 256
    for char in l:
        charCode = ord(char)
        if buf[charCode]: # Found character we already seen.
            return False
        else:
            buf[charCode] = True # Found new character, mark it as seen.
    return True

class UniqueCharacterTest(unittest.TestCase):

    def test_unique(self):
        l = 'abc'
        self.assertTrue(unique(l))

    def test_not_unique(self):
        l = 'aaa'
        self.assertFalse(unique(l))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
