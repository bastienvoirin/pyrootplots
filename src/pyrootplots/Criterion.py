#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyrootplots.Condition import Condition

class Criterion:
    def __init__(self,
                 condition: Condition):
        """
        Args:
            condition (Condition):
        """
        self.condition = condition

    def __str__(self):
        """Concise string representation of an instance."""
        if self.condition == Condition.LESS_THAN:
            return f"{variableName} < {self.values[0]}"
        if self.condition == Condition.LESS_THAN_OR_EQUAL_TO:
            return f"{variableName} <= {self.values[0]}"
        if self.condition == Condition.GREATER_THAN:
            return f"{variableName} > {self.values[0]}"
        if self.condition == Condition.GREATER_THAN_OR_EQUAL_TO:
            return f"{variableName} >= {self.values[0]}"
        if self.condition == Condition.IN_RANGE_OPEN_OPEN:
            return f"{self.values[0]} < {variableName} < {self.values[1]}"
        if self.condition == Condition.IN_RANGE_OPEN_CLOSED:
            return f"{self.values[0]} < {variableName} <= {self.values[1]}"
        if self.condition == Condition.IN_RANGE_CLOSED_OPEN:
            return f"{self.values[0]} <= {variableName} < {self.values[1]}"
        if self.condition == Condition.IN_RANGE_CLOSED_CLOSED:
            return f"{self.values[0]} <= {variableName} <= {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_OPEN_OPEN:
            return f"{variableName} <= {self.values[0]} or {variableName} >= {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_OPEN_CLOSED:
            return f"{variableName} <= {self.values[0]} or {variableName} > {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_CLOSED_OPEN:
            return f"{variableName} < {self.values[0]} or {variableName} >= {self.values[1]}"
        if self.condition == Condition.NOT_IN_RANGE_CLOSED_CLOSED:
            return f"{variableName} < {self.values[0]} or {variableName} > {self.values[1]}"
        raise ValueError

    def __repr__():
        """Complete string representation of an instance."""
        return "\n".join([f"Criterion(condition = {self.condition})"])
