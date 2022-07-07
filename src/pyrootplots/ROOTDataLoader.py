#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import ROOT
from ROOT import RDataFrame
import uproot
import pandas

class ROOTDataLoader:
    def __init__(self,
                 files,
                 tree:      str,
                 variables: list[str] = []):
        """Utility class to load ROOT files as ``pandas.DataFrame`` objects.
        
        Args:
            files:
                Files.
            tree:
                Tree.
            variables:
                List of variable names.
        
        Example::
        
            >>> from pyrootplots.ROOTDataLoader import ROOTDataLoader
            >>> rdl = ROOTDataLoader("filename.root", "tree_name", ["eta", "phi"])
            >>> pdf = rdl.getPandasDataFrame()
            >>> print(pdf)
        """
        self.files     = files
        self.tree      = tree
        self.variables = variables

    def getPandasDataFrame(self,
                           returnTree: bool = False):
        """Reads data from a ROOT file as a pandas DataFrame object.
        
        Args:
            returnTree (bool):
                Whether.
        """
        ret = {}
        rdf = RDataFrame(self.tree, self.files)
        for var in self.variables:
            ndf = rdf.AsNumpy([var])
            pdf = pandas.DataFrame(ndf)
            ret[var] = pdf

        if returnTree:
            return ret, None # TODO: return dict of TTree objects
        return ret

    @staticmethod
    def fromFile(filename:  str,
                 histnames: list[str],
                 debug:     bool = False):
        """Fetch histograms from a ROOT file.
        
        Args:
            filename:
               Path and name of the ROOT file to read.
            histnames:
               Names of the histograms to load from the ROOT file.
            debug:
                If ``True``, the structure of the ROOT file will be printed.
        
        Example::
        
            >>> from pyrootplots.Histogram1D import Histogram1D
            >>> histograms = Histogram1D.fromFile("filename.ROOT", ["hist1", "hist2", "hist3"])
            >>> hist1 = histograms["hist1"]
            >>> hist2 = histograms["hist2"]
            >>> hist3 = histograms["hist3"]
        """
        rootfile = uproot.open(filename)
        if debug:
            print(*rootfiles.classnames(), sep="\n")
        histograms = {}
        for histname in histnames:
            hist = rootfile[histname]
            histograms[histname] = hist
        return histograms
