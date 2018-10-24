# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 02:18:27 2018

@author: Leandro
"""

# A regular polygon has n number of sides. Each side has length s.
#
# -The area of a regular polygon is:
#
# -The perimeter of a polygon is: length of the boundary of the polygon
#
# Write a function called polysum that takes 2 arguments, n and s. This
# function should sum the area and square of the perimeter of the regular
# polygon. The function returns the sum, rounded to 4 decimal places.

from math import tan, pi

def polysum(n, s):
    """
    Return the the perimeter squared plus the area of the regular polygon that
    has n sides of length s, rounded to 4 decimal places.

    Arguments:
    n (int): Number of sides of the regular polygon. Must be greater than 2.
    s (float): Length of a side of the regular polygon. Must be greater than 0
    """
    return round( (s*n)**2 + (0.25*n*s**2)/tan(pi/n), 4)
