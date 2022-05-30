#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

from Cut import Cut

class ROCCurve:
    def __init__(self,
                 cuts: list[Cut]):
        """Receiver operating characteristic curve."""
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
