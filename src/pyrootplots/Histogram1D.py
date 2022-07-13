#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
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
                 density: bool        = False,
                 style:   str         = "both",
                 color:   list[str]   = [],
                 label:   list[str]   = [],
                 legend:  dict        = {},
                 scale:   list[float] = [],
                 binned:  bool        = False):
        """1D histogram.
        
        Args:
            data (list[pandas.DataFrame]):
                List of data to fill histogram 
            weights (list[pandas.DataFrame]):
                Multiply each bin by the value of the weighted bin. The shape of the weights list must be equal to that of the data.
                If no weights is needed, default is set to 1.
            bins (int):
                Number of bins for histogram.   
            binned (bool):
                Set to ``True`` if ``data`` is already the population of each bin.    
            xmin (float):
                Minimum x-axis value.
            xmax (float):
                Maximum x-axis value.
            logx (bool):
                Set x-axis to log scale.
            logy (bool):
                Set y-axis to log scale.
            stacked (bool):
                Set to ``True`` if one wants to stack distributions. The default is set to ``False``.
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
            legend (dict):
                Keyword arguments passed to ``self.ax.legend()``.
            scale (list[float]):
                List of coefficients used to scale to luminosity.
        """

        self.data    = data
        self.weights = weights
        self.bins    = bins
        self.binned  = binned
        self.xmin    = xmin
        self.xmax    = xmax
        self.logx    = logx
        self.logy    = logy
        self.stacked = stacked
        self.density = density
        self.style   = style
        self.color   = color
        self.label   = label
        self.legend  = legend
        self.scale   = scale

    def __str__(self):
        """Concise string representation of an instance."""
        return "Histogram1D(...)" # TODO

    def __repr__(self):
        """Complete string representation of an instance."""
        return "Histogram1D(...)" # TODO

    def unitWeight(self,
                   length:  int,
                   dataset: int):
        """
        """
        return pd.DataFrame(data=np.full(length, 1 if not self.scale else self.scale[dataset]))

    def plot(self,
             ax,
             title                      = None,
             titleloc:            str   = "center",
             titlefontsize:       str   = "medium",
             titlepad                   = None,
             xlabel                     = None,
             xlabelloc:           str   = "right",
             ylabel                     = None,
             ylabelloc:           str   = "top",
             overlayfirstdataset: bool  = False,
             overlayscale:        int   = 1,
             xylabelfontsize:     str   = "medium"):
        """
        """
        self.ax = ax

        if title:
            self.ax.set_title(label    = title,
                              loc      = titleloc,
                              fontsize = titlefontsize,
                              pad      = titlepad)
        if xlabel:
            self.ax.set_xlabel(xlabel   = xlabel,
                               loc      = xlabelloc,
                               fontsize = xylabelfontsize)
        if ylabel:
            self.ax.set_ylabel(ylabel   = ylabel,
                               loc      = ylabelloc,
                               fontsize = xylabelfontsize)

        if not self.binned:
            print(*[d.shape for d in pd.DataFrame(self.data)], sep=",")
            print(*[w.shape for w in pd.DataFrame(self.weights)], sep=",")
            for i in range(len(self.weights)):
                if self.weights[i] is 1:
                    self.weights[i] = self.unitWeight(self.data[i].shape[0], i)
            print(*[w.shape for w in pd.DataFrame(self.weights)], sep=",")

            mergedData    = pd.concat(self.data[:],    axis=1)
            mergedWeights = pd.concat(self.weights[:], axis=1)
            print(mergedData.shape)
            print(mergedWeights.shape)

            # fill
            if self.style in ("filled", "both"):
                self.ax.hist(x        = mergedData,
                             bins     = self.bins,
                             range    = (self.xmin, self.xmax),
                             density  = self.density,
                             weights  = mergedWeights,
                             histtype = "stepfilled",
                             color    = self.color,
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
                             stacked  = self.stacked)

            # Overlay first dataset?
            # fill
            if overlayfirstdataset and (self.style in ("filled", "both")):
                self.ax.hist(x        = self.data[0], # TODO: scale the overlay by overlayscale
                             bins     = self.bins,
                             range    = (self.xmin, self.xmax),
                             density  = self.density,
                             weights  = self.weights[0],
                             histtype = "stepfilled",
                             color    = self.color[0])
            # outline
            if overlayfirstdataset and (self.style in ("outlined", "both")):
                self.ax.hist(x        = self.data[0], # TODO: scale the overlay by overlayscale
                             bins     = self.bins,
                             range    = (self.xmin, self.xmax),
                             density  = self.density,
                             weights  = self.weights[0],
                             histtype = "step",
                             color    = "black")
        else: # data is already binned
            mergedScaledData = pd.concat([data for (scale, data) in zip(self.scale, self.data)], axis=1)
            print(f"mergedScaledData.shape = {mergedScaledData.shape}")
            mergedScaledData = mergedScaledData[::-1]
            print(f"mergedScaledData.shape = {mergedScaledData.shape}")
            binsEdges = np.linspace(start=self.xmin, stop=self.xmax, num=self.bins)
            mergedBinsEdges = b = np.tile(binsEdges, (len(self.data), 1)).T
            print(f"mergedBinsEdges.shape = {mergedBinsEdges.shape}")
            # both filled and outlined
            if self.style == "both":
                self.ax.hist(x         = mergedBinsEdges,
                             bins      = self.bins,
                             range     = (self.xmin, self.xmax),
                             density   = self.density,
                             weights   = mergedScaledData,
                             histtype  = "stepfilled",
                             color     = self.color,
                             stacked   = self.stacked,
                             edgecolor = "k")
            # filled
            if self.style == "filled":
                self.ax.hist(x        = mergedBinsEdges,
                             bins     = self.bins,
                             range    = (self.xmin, self.xmax),
                             density  = self.density,
                             weights  = mergedScaledData,
                             histtype = "stepfilled",
                             color    = self.color,
                             stacked  = self.stacked)
            # outlineed
            if self.style == "outlined":
                pass # TODO

        self.ax.set_xlim(xmin = self.xmin,
                         xmax = self.xmax)

        if self.style == "both":
            colors, ecs = self.color, ["k"] * len(self.color)
        elif self.style == "filled":
            colors, ecs = self.color, [None] * len(self.color)
        elif self.style == "outlined":
            colors, ecs = [None] * len(self.color), self.color
        else:
            raise ValueError(f"self.style, which is {self.style.__repr__()}, is not in ('filled', 'outlined', 'both')")
        handles = [Rectangle((0, 0), 1, 1, color=color, ec=ec) for (color, ec) in zip(colors, ecs)]
        self.ax.legend(handles, labels=self.label, **self.legend)

        return self
