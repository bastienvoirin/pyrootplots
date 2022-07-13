#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from enum import Enum

class BaseColor(Enum):
    """BaseColor.

    Example::

        >>> from pyrootplots.Color import BaseColor, Color
        >>> BaseColor
        <enum 'BaseColor'>
        >>> red = BaseColor.RED
        >>> red
        <BaseColor.RED: (255, 0, 0)>
        >>> red.name
        'RED'
        >>> red.value
        (255, 0, 0)
        >>> magentaPlus3 = Color(BaseColor.MAGENTA, 3)
        >>> magentaPlus3
        Color(baseColor=BaseColor.MAGENTA, shift=3)
        >>> print(magentaPlus3)
        Color.BaseColor.MAGENTA+3

    """
    RED     = (255,   0,   0)
    ORANGE  = (255, 153, 102)
    YELLOW  = (255, 255,   0)
    SPRING  = (204, 255, 102)
    GREEN   = (  0, 255,   0)
    TEAL    = (102, 255, 153)
    CYAN    = (  0, 255, 255)
    AZURE   = (102, 204, 255)
    BLUE    = (  0,   0, 255)
    VIOLET  = (153, 102, 255)
    MAGENTA = (255,  0,  255)
    PINK    = (255,  0,  255)

    WHITE   = (255, 255, 255)
    BLACK   = (  0,   0,   0)

class Color:
    RED     = BaseColor.RED
    ORANGE  = BaseColor.ORANGE
    YELLOW  = BaseColor.YELLOW
    SPRING  = BaseColor.SPRING
    GREEN   = BaseColor.GREEN
    TEAL    = BaseColor.TEAL
    CYAN    = BaseColor.CYAN
    AZURE   = BaseColor.AZURE
    BLUE    = BaseColor.BLUE
    VIOLET  = BaseColor.VIOLET
    MAGENTA = BaseColor.MAGENTA
    PINK    = BaseColor.PINK

    WHITE   = BaseColor.WHITE
    BLACK   = BaseColor.BLACK
    
    def __init__(self,
                 baseColor: BaseColor = BaseColor.WHITE,
                 shift:     int       = 0):
        """Color.

        Args:
            baseColor (str):
                Base color.
        """
        self.baseColor = baseColor
        self.shift     = shift

    def __str__(self):
        """Concise string representation of an instance."""
        return f"Color({self.baseColor})" + (f"{self.shift:+}" if self.shift != 0 else "")

    def __repr__(self):
        """Complete string representation of an instance."""
        return f"Color(baseColor={self.baseColor}, shift={self.shift})"

    def toRGBint(self):
        """

        """
        return

    def toRGBfloat(self):
        """

        """
        return tuple(channel / 255 for channel in self.toRGBint())

    def __add__(self,
                shift: int):
        self.shift += shift
        return

    def __sub__(self,
                shift: int):
        self.shift -= shift
        return
