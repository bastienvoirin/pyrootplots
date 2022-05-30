#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Condition import Condition

class Cut:
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
        A cut is defined by a variable name (on which the cut is applied) and 1 or 2 values
        (defining the criterion). The number of signal and background events before and after the
        cut must be specified.
        
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

    def __str__(self):
        """Concise string representation of an instance."""
        return ""

    def __repr__(self):
        """Complete string representation of an instance."""
        return "\n,".join([f"Cut(variableName = {self.variableName}",
                           f"    cutValues    = {self.cutValues}",
                           f"    condition    = {self.condition}",
                           f"    sigEvtBefore = {self.sigEvtBefore}",
                           f"    sigEvtAfter  = {self.sigEvtAfter}",
                           f"    bkgEvtBefore = {self.bkgEvtBefore}",
                           f"    bkgEvtAfter  = {self.bkgEvtAfter}",
                           f"    sigScale     = {self.sigScale}",
                           f"    bkgScale     = {self.bkgScale}",
                           f"    scale        = {self.scale})"])
