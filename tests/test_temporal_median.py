# -*- coding: utf-8 -*-
"""Unittest file for range filter.
"""

import unittest
import lidar_filter.temporal_median as tm

import numpy as np


class TestUM(unittest.TestCase):
    """Unit test for range filter

    """

    def test_simple(self):
        """Unit test for range filter
        From problem example
        """

        tmed = tm.TemporalMedianFilter(3)
        test_list = [
            ([0.0, 1.0, 2.0, 1.0, 3.0], [0.0, 1.0, 2.0, 1.0, 3.0]),
            ([1.0, 5.0, 7.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0]),
            ([2.0, 3.0, 4.0, 1.0, 0.0], [1.0, 3.0, 4.0, 1.0, 3.0]),
            ([3.0, 3.0, 3.0, 1.0, 3.0], [1.5, 3.0, 3.5, 1.0, 3.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [2.5, 3.0, 4.0, 1.0, 1.5])
        ]

        for i, out in test_list:
            self.assertTrue(np.alltrue(tmed.update(np.array(i)) == np.array(out)))

    def test_single(self):
        """Unit test for range filter
        tests a single input
        """

        tmed = tm.TemporalMedianFilter(3)
        test_list = [
            ([0.0, 1.0, 2.0, 1.0, 3.0], [0.0, 1.0, 2.0, 1.0, 3.0]),
        ]

        for i, out in test_list:
            self.assertTrue(np.alltrue(tmed.update(np.array(i)) == np.array(out)))

    def test_double(self):
        """Unit test for range filter
        tests two inputs
        """

        tmed = tm.TemporalMedianFilter(3)
        test_list = [
            ([0.0, 1.0, 2.0, 1.0, 3.0], [0.0, 1.0, 2.0, 1.0, 3.0]),
            ([1.0, 5.0, 7.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0]),
        ]

        for i, out in test_list:
            self.assertTrue(np.alltrue(tmed.update(np.array(i)) == np.array(out)))

    def test_tripple(self):
        """Unit test for range filter
        tests three inputs
        """

        tmed = tm.TemporalMedianFilter(3)
        test_list = [
            ([0.0, 1.0, 2.0, 1.0, 3.0], [0.0, 1.0, 2.0, 1.0, 3.0]),
            ([1.0, 5.0, 7.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0]),
            ([2.0, 3.0, 4.0, 1.0, 0.0], [1.0, 3.0, 4.0, 1.0, 3.0]),
        ]

        for i, out in test_list:
            self.assertTrue(np.alltrue(tmed.update(np.array(i)) == np.array(out)))

    def test_steady_state(self):
        """Unit test for range filter
        tests many inputs in a steady state for values
        """

        tmed = tm.TemporalMedianFilter(3)
        test_list = [
            ([0.0, 1.0, 2.0, 1.0, 3.0], [0.0, 1.0, 2.0, 1.0, 3.0]),
            ([1.0, 5.0, 7.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0]),
            ([2.0, 3.0, 4.0, 1.0, 0.0], [1.0, 3.0, 4.0, 1.0, 3.0]),
            ([3.0, 3.0, 3.0, 1.0, 3.0], [1.5, 3.0, 3.5, 1.0, 3.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [2.5, 3.0, 4.0, 1.0, 1.5]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [6.5, 2.5, 4.0, 0.5, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0]),
            ([10.0, 2.0, 4.0, 0.0, 0.0], [10.0, 2.0, 4.0, 0.0, 0.0])
        ]

        for i, out in test_list:
            self.assertTrue(np.alltrue(tmed.update(np.array(i)) == np.array(out)))

if __name__ == '__main__':
    unittest.main()
