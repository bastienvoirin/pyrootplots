#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ROOT
from ROOT import RDataFrame
import pandas

class ROOTDataLoader:
    def __init__(self,
                 tree,
                 files,
                 varWhitelist: list[str] = [],
                 varBlacklist: list[str] = []):
        """
        Args:
            tree:
            files:
            varWhitelist:
            varBlacklist:
        """
        self.tree         = tree
        self.files        = files
        self.varWhitelist = varWhitelist
        self.varBlacklist = varBlacklist

    def getPandasDataFrame(returnTree: bool = False)
        """Reads data from a ROOT file as a pandas DataFrame object.
        
        Args:
            returnTree (bool):
        """
        rdf = RDataFrame(self.tree, self.files)
        ndf = rdf.AsNumpy()
        pdf = pandas.DataFrame(ndf)
        if returnTree:
            return pdf, self.tree
        return pdf
