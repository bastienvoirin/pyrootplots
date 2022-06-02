#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
``pyrootplots`` is a plotting library for High Energy Physics. It offers
lin/log histograms, ROC curves, stack plots, and cut efficiency vs. cut value
plots from ROOT files using ``pyROOT`` and ``matplotlib``.

Usage::
    
    from pyrootplots import *
"""

import ROOT
from ROOT import TTree

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# pyrootplots' submodules/classes
from pyrootplots.Condition import Condition
from pyrootplots.Criterion import Criterion
from pyrootplots.Cut import Cut
from pyrootplots.CutEffVsVal import CutEffVsVal
from pyrootplots.Histogram1D import Histogram1D
from pyrootplots.Histogram2D import Histogram2D
from pyrootplots.ROCCurve import ROCCurve
from pyrootplots.ROOTDataLoader import ROOTDataLoader

# Print the module's docstring when using it as a script instead of a module
if __name__ == "__main__":
    print(__doc__)
