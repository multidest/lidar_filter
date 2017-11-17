# -*- coding: utf-8 -*-
"""Unittest file for range filter.
"""

import unittest
import lidar_filter.range_filter as rf

import numpy as np


class TestUM(unittest.TestCase):
    """Unit test for range filter

    """

    def test_simple(self):
        """Unit test for range filter
        simple range test
        """
        values = np.array([100, -100, 50, -50, 0])
        rfilter = rf.RangeFilter(-75, 75)
        self.assertTrue(np.alltrue(rfilter.update(values) == np.array([75, -75, 50, -50, 0])))


if __name__ == '__main__':
    unittest.main()
