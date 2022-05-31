#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

class CutEffVsVal:
    def __init__(self,
                 evtBefore:    list[float],
                 evtAfter:     list[float],
                 variableName: str,
                 yticks            = np.linspace(0.0, 1.0, 11),
                 xlabel:       str = "",
                 ylabel:       str = "events(after) / events(before)",):
        """Signal or background efficiency vs. cut value/threshold.

        Args:
            evtBefore (list[float]):
                Number of events before the cut, for each cut value.
            evtAfter (list[float]):
                Number of events after the cut, for each cut value.
            variableName (str):
                Name of the variable on which the cut is applied.
            yticks:
                Y axis ticks position.
            xlabel (str):
                X axis label.
            ylabel (str):
                Y axis label.
        """
        self.evtBefore    = evtBefore
        self.evtAfter     = evtAfter
        self.variableName = variableName
        self.yticks       = yticks
        self.xlabel       = xlabel
        self.ylabel       = ylabel

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return "\n,".join([f"CutEffVsVal(evtBefore:    {self.evtBefore}",
                           f"            evtAfter:     {self.evtAfter}",
                           f"            variableName: {self.variableName}",
                           f"            yticks:       {self.yticks}",
                           f"            xlabel:       {self.xlabel}",
                           f"            ylabel:       {self.ylabel})"])

    def plot(self,
             show: bool = False):
        """
        Args:
            show (bool):
                ``True`` to call ``plt.show()``, ``False`` otherwise.

        Returns:
            ``self``
        """
        fig, ax = plt.subplots()
        ax.set_yticks(self.yticks)
        if self.xlabel == "":
            ax.set_xlabel(self.variableName)
        else:
            ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        plt.title(self.title)
        if show:
            plt.show()
        return self

