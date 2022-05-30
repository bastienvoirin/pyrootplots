#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

class CutEffVsVal:
    def __init__(self,
                 evtBefore:    list[float],
                 evtAfter:     list[float],
                 variableName: str):
        """Signal or background efficiency vs. cut value/threshold.

        Args:
            evtBefore (list[float]):
                Number of events before the cut, for each cut value.
            evtAfter (list[float]):
                Number of events after the cut, for each cut value.
            variableName (str):
                Name of the variable on which the cut is applied.
        """
        self.evtBefore    = evtBefore
        self.evtAfter     = evtAfter
        self.variableName = variableName

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return "\n,".join([f"CutEffVsVal(evtBefore:    {self.evtBefore}",
                           f"            evtAfter:     {self.evtAfter}",
                           f"            variableName: {self.variableName})"])

    def plot(self):
        """
        """
        fig, ax = plt.subplots()
        ax.set_yticks(np.linspace(0.0, 1.0, 11))
        plt.xlabel(variableName)
        plt.ylabel("events(after) / events(before)")
        plt.title("")
        plt.show()
        return self

