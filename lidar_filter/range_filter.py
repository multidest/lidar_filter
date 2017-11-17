# -*- coding: utf-8 -*-
"""Range filter module.

This module contains a range filter for lidar range data.

"""

import numpy as np

class RangeFilter: # pylint: disable=too-few-public-methods
    """The RangeFilter class crops lidar range data

    """

    def __init__(self, min_range, max_range):
        """RangeFilter __init__ method.

        Args:
            min_range (int): min value to clip and replace lidar values.
            max_range (int): max value to clip and replace lidar values.

        """

        self.min_range = min_range
        self.max_range = max_range

    def update(self, values):
        """The update method crops data that are below a range minimum and above a 
        range maximum and replaces them with the min and max value respectivly.

        Args:
            values: (numpy.array): lidar detection values.

        Returns:
            (numpy.array): clipped values of input array

        """

        return np.clip(values, self.min_range, self.max_range)
