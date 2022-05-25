#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pyROOT/matplotlib binding module.

Plotting lin/log histograms, stack plots, ROC curves, and cut efficiency vs. cut value from ROOT
files using pyROOT and matplotlib.

Usage:
    from pyrootplots import *
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from enum import Enum

####################################################################################################

class Condition(Enum):
    """Conditions used to define cuts."""
    LESS_THAN                  =  0 # a <  b
    LESS_THAN_OR_EQUAL_TO      =  1 # a <= b
    GREATER_THAN               =  2 # a >  b
    GREATER_THAN_OR_EQUAL_TO   =  3 # a >= b
    IN_RANGE_OPEN_OPEN         =  4 # a <  b <  c
    IN_RANGE_OPEN_CLOSED       =  5 # a <  b <= c
    IN_RANGE_CLOSED_OPEN       =  6 # a <= b <  c
    IN_RANGE_CLOSED_CLOSED     =  7 # a <= b <= c
    NOT_IN_RANGE_OPEN_OPEN     =  8 # b <= a or b >= c
    NOT_IN_RANGE_OPEN_CLOSED   =  9 # b <= a or b >  c
    NOT_IN_RANGE_CLOSED_OPEN   = 10 # b <  a or b >= c
    NOT_IN_RANGE_CLOSED_CLOSED = 11 # b <  a or b >  c

####################################################################################################

class Criterion:
    def __str__(self):
        if self.condition == Condition.LESS_THAN:
            return f"{variableName} < {self.values[0]}"
        if self.condition == Condition.LESS_THAN_OR_EQUAL_TO:
            return f"{variableName} <= {self.values[0]}"
        if self.condition == Condition.GREATER_THAN:
            return f"{variableName} > {self.values[0]}"
        if self.condition == Condition.GREATER_THAN_OR_EQUAL_TO:
            return f"{variableName} >= {self.values[0]}"
        if self.condition == Condition.IN_RANGE_OPEN_OPEN:
            return f"{self.values[0]} < {variableName} < {self.values[1]}"
        if self.condition == Condition.IN_RANGE_OPEN_CLOSED:
            return f"{self.values[0]} < {variableName} < {self.values[1]}"
        if self.condition == Condition.IN_RANGE_CLOSED_OPEN:
            return f"{self.values[0]} < {variableName} < {self.values[1]}"
        if self.condition == Condition.IN_RANGE_CLOSED_CLOSED:
            return f"{self.values[0]} < {variableName} < {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_OPEN_OPEN:
            return f"{variableName} <= {self.values[0]} or {variableName} >= {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_OPEN_CLOSED:
            return f"{variableName} <= {self.values[0]} or {variableName} > {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_CLOSED_OPEN:
            return f"{variableName} < {self.values[0]} or {variableName} >= {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_CLOSED_CLOSED:
            return f"{variableName} < {self.values[0]} or {variableName} > {self.values[1]}"

####################################################################################################

class Cut:
    """
    A cut is defined by a variable name (on which the cut is applied) and 1 or 2 values (defining
    the criterion). The number of signal and background events before and after the cut must be
    specified.
    """

    def __init__(self,
                 variableName: str,
                 cutValues:    list[float],
                 condition:    Condition,
                 sigEvtBefore: float,
                 sigEvtAfter:  float,
                 bkgEvtBefore: dict[str, float],
                 bkgEvtAfter:  dict[str, float],
                 sigScale:     float = 1.0,
                 bkgScale:     list[float] = [1.0],
                 scale:        bool = False):
        """
        Args:
            variableName (str):
                Name of the variable on which the cut is applied.
            cutValues (list(float)):
                Thresholds of the cut (1 or 2 values).
            condition (Condition):
            sigEvtBefore (float):
                Number of signal events before the cut.
            sigEvtAfter (float):
                Number of signal events after the cut.
            bkgEvtBefore (dict(str, float)):
                Number of background events before the cut, for each background.
            bkgEvtAfter (dict(str, float)):
                Number of background events after the cut, for each background.
            sigScale (float, optional):
                Scaling to luminosity factor for the signal.
            bkgScale (list(float), optional):
                Scaling to luminosity factor for each background.
            scale (bool, optional):
                Whether or not the numbers displayed should be scaled to luminosity or not.

        Returns:
        """
        self.variableName = variableName
        self.cutValues    = cutValues
        self.condition    = condition
        self.sigEvtBefore = sigEvtBefore
        self.sigEvtAfter  = sigEvtAfter
        self.bkgEvtBefore = bkgEvtBefore
        self.bkgEvtAfter  = bkgEvtAfter
        self.sigScale     = sigScale
        self.bkgScale     = bkgScale
        self.scale        = scale
        return

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return "\n".join([f"Cut(variableName = {self.variableName},",
                          f"    cutValues    = {self.cutValues},",
                          f"    condition    = {self.condition},",
                          f"    sigEvtBefore = {self.sigEvtBefore},",
                          f"    sigEvtAfter  = {self.sigEvtAfter},",
                          f"    bkgEvtBefore = {self.bkgEvtBefore},",
                          f"    bkgEvtAfter  = {self.bkgEvtAfter},",
                          f"    sigScale     = {self.sigScale},",
                          f"    bkgScale     = {self.bkgScale},",
                          f"    scale        = {self.scale})"])

####################################################################################################

class ROCCurve:
    """Receiver operating characteristic curve."""

    def __init__(self,
                 cuts: list[Cut]):
        """
        """
        return

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return ""

    def plot(self):
        """
        """
        fig, ax = plt.subplots()
        ax.set_xticks(np.linspace(0.0, 1.0, 11))
        ax.set_yticks(np.linspace(0.0, 1.0, 11))
        plt.xlabel("B(after) / B(before)")
        plt.ylabel("S(after) / S(before)")
        plt.title("")
        plt.show()
        return

####################################################################################################

class EfficiencyVsCutValue:
    """Signal or background efficiency vs. cut value/threshold."""

    def __init__(self,
                 evtBefore:    list[float],
                 evtAfter:     list[float],
                 variableName: str):
        """
        """
        self.evtBefore = evtBefore
        self.evtAfter  = evtAfter
        return

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return ""

    def plot(self):
        """
        """
        fig, ax = plt.subplots()
        ax.set_yticks(np.linspace(0.0, 1.0, 11))
        plt.xlabel(variableName)
        plt.ylabel("events(after) / events(before)")
        plt.title("")
        plt.show()
        return

####################################################################################################

class Histogram1D:
    """1D histogram.
    """

    def __init__(self):
        """
        """
        return

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return ""

####################################################################################################

class Histogram2D:
    """2D histogram.
    """

    def __init__(self):
        """
        """
        return

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return ""

####################################################################################################

if __name__ == "__main__":
    print(__doc__)
