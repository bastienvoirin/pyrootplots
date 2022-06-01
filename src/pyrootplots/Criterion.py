#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyrootplots.Condition import Condition

class Criterion:
    def __init__(self,
                 variableName: str,
                 condition:    Condition,
                 values:       list[str]):
        """
        Args:
            variableName (str):
                Variable name.
            condition (Condition):
                Condition.
            values (list(str)):
                Values.

        Example:
            
            >>> from pyrootplots import Criterion
            >>> from pyrootplots import Condition
            >>> crit = Criterion("eta", Condition.LESS_THAN_OR_EQUAL_TO, [2.5])
            >>> print(crit)
            eta <= 2.5
            
        """
        self.variableName = variableName
        self.condition    = condition
        self.values       = values

    def __str__(self):
        """Concise string representation of an instance."""
        if self.condition == Condition.LESS_THAN:
            return f"{self.variableName} < {self.values[0]}"
        if self.condition == Condition.LESS_THAN_OR_EQUAL_TO:
            return f"{self.variableName} <= {self.values[0]}"
        if self.condition == Condition.GREATER_THAN:
            return f"{self.variableName} > {self.values[0]}"
        if self.condition == Condition.GREATER_THAN_OR_EQUAL_TO:
            return f"{self.variableName} >= {self.values[0]}"
        if self.condition == Condition.IN_RANGE_OPEN_OPEN:
            return f"{self.values[0]} < {self.variableName} < {self.values[1]}"
        if self.condition == Condition.IN_RANGE_OPEN_CLOSED:
            return f"{self.values[0]} < {self.variableName} <= {self.values[1]}"
        if self.condition == Condition.IN_RANGE_CLOSED_OPEN:
            return f"{self.values[0]} <= {self.variableName} < {self.values[1]}"
        if self.condition == Condition.IN_RANGE_CLOSED_CLOSED:
            return f"{self.values[0]} <= {self.variableName} <= {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_OPEN_OPEN:
            return " or ".join([f"{self.variableName} <= {self.values[0]}",
                                f"{self.variableName} >= {self.values[1]}"])
        if self.condition == Condition.NOT_IN_RANGE_OPEN_CLOSED:
            return " or ".join([f"{self.variableName} <= {self.values[0]}",
                                f"{self.variableName} > {self.values[1]}"])
        if self.condition == Condition.NOT_IN_RANGE_CLOSED_OPEN:
            return " or ".join([f"{self.variableName} < {self.values[0]}",
                                f"{self.variableName} >= {self.values[1]}"])
        if self.condition == Condition.NOT_IN_RANGE_CLOSED_CLOSED:
            return " or ".join([f"{self.variableName} < {self.values[0]}",
                                f"{self.variableName} > {self.values[1]}"])
        raise ValueError

    def __repr__():
        """Complete string representation of an instance."""
        return ",\n".join([f"Criterion(variableName = {self.variableName}",
                           f"          condition    = {self.condition}",
                           f"          values       = {self.values})"])
