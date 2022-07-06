#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from matplotlib import pyplot as plt
import pandas as pd

class Histogram1D:
    def __init__(self,
                 data: list[pd.DataFrame],
                 weights: list[pd.DataFrame],
                 bins: int,
                 xmin: float,
                 xmax: float,
                 logx: bool,
                 logy: bool,
                 stacked: bool,
                 density: bool = False,
                 histStyle: str = 'bar',
                 color: list[str] = [],
                 labels: list[str] = [],
                 makeLegend: bool = True
                 ):
        """1D histogram.
        
        Args:
            data (list[pandas.DataFrame]):
                List of data to fill histogram 
            weights (list[pandas.DataFrame]):
                Multiply each bin by the value of the weighted bin. The shape of the weights list must be equal to that of the data.
                If no weights is needed, default is set to 1.
            bins (int):
                Number of bins for histogram.        
            xmin (float):
                Minimum x-axis value.
            xmax (float):
                Maximum x-axis value.
            logx (bool):
                Set x-axis to log scale.
            logy (bool):
                Set y-axis to log scale.
            stacked (bool):
                Set to True if one wants to stack distributions. The default is set to False.
            density (bool):
                Integrates the histogram to 1: as density = counts / (sum(counts) * np.diff(bins)).
                By default set to False.
            histStyle (str):
                The type of histogram to draw.
                    'bar' is a traditional bar-type histogram. If multiple data are given the bars are arranged side by side.
                    'barstacked' is a bar-type histogram where multiple data are stacked on top of each other.
                    'step' generates a lineplot that is by default unfilled.
                    'stepfilled' generates a lineplot that is by default filled.
            color (list[str]):
                Color or sequence of colors, one per dataset.
            makeLegend (bool):
                Bool to set legend.
        """

        self.data       = data
        self.weights    = weights
        self.bins       = bins
        self.xmin       = xmin
        self.xmax       = xmax
        self.logx       = logx
        self.logy       = logy
        self.stacked    = stacked
        self.density    = density
        self.histStyle  = histStyle
        self.color      = color
        self.labels     = labels


    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return ""

    def unitWeight(self, lenghtOfData: float):
        """
        """
        self.lenghtOfData = lenghtOfData

        x = []
        for i in range(lenghtOfData):
            x.append(1)
        unitWeight = pd.DataFrame(data=x)

        return unitWeight

    def writeLegend(self,
                    ax,
                    labels:           list[str] = [],
                    title:            str       = "",
                    position:         str       = "upper right",
                    ncols:            int       = 1,
                    spaceBetweenCols: float     = 0.8,
                    shadow:           bool      = False,
                    facecolor:        str       = "inherit",
                    edgecolor:        str       = "0.8"):
        """
        """
        self.labels           = labels
        self.title            = title
        self.position         = position
        self.ncols            = ncols
        self.spaceBetweenCols = spaceBetweenCols
        self.shadow           = shadow
        self.facecolor        = facecolor
        self.edgecolor        = edgecolor

        # Still to do...
        
        return self

    def plot(self, ax):
        """
        """
        self.ax = ax

        for i in range(len(self.weights)):
            lenght = self.data[i].shape[0]
            if self.weights[i] is 1:
                self.weights[i] = self.unitWeight(lenght)

        mergedData = pd.concat(self.data[:], axis=1)
        mergedWeights = pd.concat(self.weights[:], axis=1)

        self.ax.hist(x        = mergedData,
                     bins     = self.bins,
                     stacked  = self.stacked,
                     range    = (self.xmin, self.xmax),
                     density  = self.density,
                     weights  = mergedWeights,
                     histtype = self.histStyle,
                     color    = self.color)
        self.ax.legend(labels = self.labels)
        
        return self
