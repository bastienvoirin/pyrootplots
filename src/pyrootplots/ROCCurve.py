#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

from .Cut import Cut

class ROCCurve:
    def __init__(self,
                 cuts:      list[Cut],
                 title:     str         = "ROC curve",
                 xlabel:    str         = "B(after) / B(before)",
                 ylabel:    str         = "S(after) / S(before)",
                 xticks                 = np.linspace(0.0, 1.0, 11),
                 yticks                 = np.linspace(0.0, 1.0, 11),
                 xlim:      list[float] = [0.0, 1.0],
                 ylim:      list[float] = [0.0, 1.0],
                 minorGrid: dict        = {},
                 majorGrid: dict        = {},
                 scatter:   dict        = {}):
        """Receiver operating characteristic curve.

        Args:
            cuts (list[Cut]):
                List of the cuts to place on the ROC curve.
            title (str):
                Title of the ROC curve.
            xlabel (str):
                X axis label.
            ylabel (str):
                Y axis label.
            xticks:
                X axis ticks position.
            yticks:
                Y axis ticks position.
            xlim (list(str)):
                X axis boundaries.
            ylim (list(str)):
                Y axis boundaries.
            minorGrid:
                Parameters passed to ``plt.grid(which = "minor")``.
            majorGrid:
                Parameters passed to ``plt.grid(which = "major")``.
            scatter:
                Parameters passed to ``plt.scatter()``.
        """
        self.cuts      = cuts
        self.title     = title
        self.xlabel    = xlabel
        self.ylabel    = ylabel
        self.xticks    = xticks
        self.yticks    = yticks
        self.minorGrid = minorGrid
        self.majorGrid = majorGrid
        self.scatter   = scatter

    def __str__(self):
        """Concise string representation of an instance."""
        return f"{self.ylabel} = f({self.xlabel}) for cuts {self.cuts}"

    def __repr__(self):
        """Complete string representation of an instance."""
        return "\n,".join([f"ROCCurve(cuts   = {self.cuts}",
                           f"         xlabel = {self.xlabel}",
                           f"         ylabel = {self.ylabel}",
                           f"         xticks = {self.xticks}",
                           f"         yticks = {self.yticks})"])

    def plot(self,
             fig        = None,
             ax         = None,
             show: bool = False):
        """Plots signal efficiency vs. background efficiency for each cut.

        Args:
            fig:
                matplotlib Figure object.
            ax:
                matplotlib Axes object.
            show (bool):
                ``True`` to call ``plt.show()``, ``False`` otherwise.

        Returns:
            ``self``
        """
        if fig is None or ax is None:
            fig, ax = plt.subplots()
        ax.set_title(self.title)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_xticks(self.xticks)
        ax.set_yticks(self.yticks)
        ax.grid(which = "major", **self.majorGrid)
        ax.grid(which = "minor", **self.minorGrid)
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.0])
        ax.scatter(x = [bkgEvtAfter / bkgEvtBefore for cut in self.cuts],
                   y = [sigEvtAfter / sigEvtBefore for cut in self.cuts],
                   **self.scatter)
        if show:
            plt.show()
        return self
