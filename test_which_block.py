#!/usr/bin/env python

import unittest
import which_block

class TestRoundUp(unittest.TestCase):
    def test_param(self):
        self.assertRaises(TypeError, which_block.round_up, None ) #throws expected error if called with no params
        self.assertEqual(which_block.round_up(0), 0)              #can handle zero correctly
        self.assertNotEqual(which_block.round_up(1), 0)           
        self.assertEqual(which_block.round_up(2.5), 3)

if __name__ == '__main__':
    unittest.main()
