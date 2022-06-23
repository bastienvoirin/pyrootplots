#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ROOT
from ROOT import RDataFrame
import pandas

class ROOTDataLoader:
    def __init__(self,
                 files,
                 tree:      str,
                 variables: list[str] = []):
        """
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

    def getPandasDataFrame(self, returnTree: bool = False):
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
