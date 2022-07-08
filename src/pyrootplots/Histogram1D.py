
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from matplotlib import pyplot as plt
import pandas as pd

class Histogram1D:
    def __init__(self,
                 data:    list[pd.DataFrame],
                 weights: list[pd.DataFrame],
                 bins:    int,
                 xmin:    float,
                 xmax:    float,
                 logx:    bool,
                 logy:    bool,
                 stacked: bool,
                 density: bool      = False,
                 style:   str       = "both",
                 color:   list[str] = [],
                 label:   list[str] = []):
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
            style (str):
                The type of histogram to draw.
                    - "filled" is a traditional contiguous bar-type bar histogram.
                    - "outlined" is a lineplot.s
                    - "both" draws a filled (contiguous bar-type) histogram with a black outline.
            color (list[str]):
                Color or sequence of colors, one per dataset.
            label (list[str]):
                Label or list of labels corresponding to the input data.
        """

        self.data    = data[::-1]
        self.weights = weights[::-1]
        self.bins    = bins
        self.xmin    = xmin
        self.xmax    = xmax
        self.logx    = logx
        self.logy    = logy
        self.stacked = stacked
        self.density = density
        self.style   = style
        self.color   = color[::-1]
        self.label   = label[::-1]


    def __str__(self):
        """Concise string representation of an instance."""
        return "" # TODO

    def __repr__(self):
        """Complete string representation of an instance."""
        return "" # TODO

    def unitWeight(self,
                   lengthOfData: int):
        """
        """
        self.lengthOfData = lengthOfData

        x = []
        for i in range(lengthOfData):
            x.append(1)
        unitWeight = pd.DataFrame(data=x)

        return unitWeight

    def plot(self,
             ax,
             title  = None,
             xlabel = None,
             ylabel = None,
             axisLabelFontSize:   str  = "medium",
             overlayFirstDataset: bool = False):
        """
        """
        self.ax = ax

        if title:
            self.ax.set_title(title)
        if xlabel:
            self.ax.set_xlabel(xlabel, fontsize=axisLabelFontSize)
        if ylabel:
            self.ax.set_ylabel(ylabel, fontsize=axisLabelFontSize)

        for i in range(len(self.weights)):
            length = self.data[i].shape[0]
            if self.weights[i] is 1:
                self.weights[i] = self.unitWeight(length)

        mergedData    = pd.concat(self.data[:],    axis=1)
        mergedWeights = pd.concat(self.weights[:], axis=1)

        # fill
        if self.style in ("filled", "both"):
            self.ax.hist(x        = mergedData,
                         bins     = self.bins,
                         range    = (self.xmin, self.xmax),
                         density  = self.density,
                         weights  = mergedWeights,
                         histtype = "stepfilled",
                         color    = self.color,
                         label    = self.label,
                         stacked  = self.stacked)
        # outline
        if self.style in ("outlined", "both"):
            self.ax.hist(x        = mergedData,
                         bins     = self.bins,
                         range    = (self.xmin, self.xmax),
                         density  = self.density,
                         weights  = mergedWeights,
                         histtype = "step",
                         color    = ["black"] * len(self.data),
                         label    = self.label if self.style == "outlined" else None,
                         stacked  = self.stacked)

        # Overlay first dataset?
        # fill
        if overlayFirstDataset and (self.style in ("filled", "both")):
            self.ax.hist(x        = self.data[-1],
                         bins     = self.bins,
                         range    = (self.xmin, self.xmax),
                         density  = self.density,
                         weights  = self.weights[-1],
                         histtype = "stepfilled",
                         color    = self.color[-1])
        # outline
        if overlayFirstDataset and (self.style in ("outlined", "both")):
            self.ax.hist(x        = self.data[-1],
                         bins     = self.bins,
                         range    = (self.xmin, self.xmax),
                         density  = self.density,
                         weights  = self.weights[-1],
                         histtype = "step",
                         color    = "black")
        
        self.ax.set_xlim(xmin = self.xmin,
                         xmax = self.xmax)
        return self
