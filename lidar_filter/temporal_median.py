# -*- coding: utf-8 -*-
"""temporal median filter module.

This module calculates the temporal median for a given window over a 2D lidar point scan.

"""

import numpy as np

class TemporalMedianFilter: # pylint: disable=too-few-public-methods
    """The temporal median filter returns the median of the current and the previous D scans

    """

    def __init__(self, D_scans):
        """TemporalMedianFilter __init__ method.

        Args:
            D_scans (int): size of window for median filtering.

        """

        if D_scans <= 0 :
            raise ValueError("D_scans must be greater than 0")

        self.d_scans = D_scans
        self.cma_n = None

        # count: (int): for edge case where len(cma_n) < D_scans
        self.count = 0

    def update(self, values):
        """The update method shifts the rollbuffer and updates the current data.

        Args:
            values: (np.array): lidar hits.

        Returns:
            (np.array): temporal median of d_scan previous values

        """

        #handles edge case for first lidar scan
        if self.cma_n is None:
            self.cma_n = np.zeros((self.d_scans+1, values.shape[0]))

        #shift the cma_n buffer and update with values
        self.cma_n = np.roll(self.cma_n, 1, axis=0)
        self.cma_n[0] = values

        # for edge case where len(cma_n) < D_scans
        if self.count <= self.d_scans:
            self.count += 1

        return np.median(self.cma_n[:self.count], axis=0)
