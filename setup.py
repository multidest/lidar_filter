# -*- coding: utf-8 -*-
"""lidar filter setup module.

"""

import os
from setuptools import setup

def read(file_name):
    """helper method for setup function.

    """
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="lidar_filter",
    version="0.0.0",
    author="Abraham Hart",
    author_email="abraham.hart@gmail.com",
    description=("A small library of filters for a 2D lidar."),
    keywords="lidar filter",
    url="http://github.com/multidest/lidar_filer",
    packages=['lidar_filter'],
    long_description=read('README.md'),
)
