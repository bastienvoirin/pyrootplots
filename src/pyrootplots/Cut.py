#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Criterion import Criterion

class Cut:
    def __init__(self,
                 criterion:    Criterion, 
                 sigEvtBefore: float,
                 sigEvtAfter:  float,
                 bkgEvtBefore: dict[str, float],
                 bkgEvtAfter:  dict[str, float],
                 sigScale:     float = 1.0,
                 bkgScale:     list[float] = [1.0],
                 scale:        bool = False):
        """
        A cut is defined by a variable name (on which the cut is applied) and 1 or 2 values
        (defining the criterion). The number of signal and background events before and after the
        cut must be specified.
        
        Args:
            criterion:
                Criterion defining the cut.
            sigEvtBefore:
                Number of signal events before the cut.
            sigEvtAfter:
                Number of signal events after the cut.
            bkgEvtBefore:
                Number of background events before the cut, for each background.
            bkgEvtAfter:
                Number of background events after the cut, for each background.
            sigScale:
                Scaling to luminosity factor for the signal.
            bkgScale:
                Scaling to luminosity factor for each background.
            scale:
                Whether or not the numbers displayed should be scaled to luminosity or not.
        """
        self.criterion    = criterion
        self.sigEvtBefore = sigEvtBefore
        self.sigEvtAfter  = sigEvtAfter
        self.bkgEvtBefore = bkgEvtBefore
        self.bkgEvtAfter  = bkgEvtAfter
        self.sigScale     = sigScale
        self.bkgScale     = bkgScale
        self.scale        = scale

    def __str__(self):
        """Concise string representation of an instance."""
        return ", ".join([f"{self.criterion}",
                          f"signal: {self.sigEvtBefore} => {self.sigEvtAfter}"]
                       + [f"{bkg}: {self.bkgEvtBefore[bkg]} => {self.bkgEvtAfter[bkg]}"
                          for bkg in self.bkgEvtBefore.keys()]) + ")"

    def __repr__(self):
        """Complete string representation of an instance."""
        return ",\n".join([f"Cut(criterion    = {self.criterion}",
                           f"    sigEvtBefore = {self.sigEvtBefore}",
                           f"    sigEvtAfter  = {self.sigEvtAfter}",
                           f"    bkgEvtBefore = {self.bkgEvtBefore}",
                           f"    bkgEvtAfter  = {self.bkgEvtAfter}",
                           f"    sigScale     = {self.sigScale}",
                           f"    bkgScale     = {self.bkgScale}",
                           f"    scale        = {self.scale})"])
