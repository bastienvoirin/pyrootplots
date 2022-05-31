#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum

class Condition(Enum):
    """Conditions used to define cuts."""
    LESS_THAN                  =  0 # a <  b
    LESS_THAN_OR_EQUAL_TO      =  1 # a <= b
    GREATER_THAN               =  2 # a >  b
    GREATER_THAN_OR_EQUAL_TO   =  3 # a >= b
    IN_RANGE_OPEN_OPEN         =  4 # a <  b <  c
    IN_RANGE_OPEN_CLOSED       =  5 # a <  b <= c
    IN_RANGE_CLOSED_OPEN       =  6 # a <= b <  c
    IN_RANGE_CLOSED_CLOSED     =  7 # a <= b <= c
    NOT_IN_RANGE_OPEN_OPEN     =  8 # b <= a or b >= c
    NOT_IN_RANGE_OPEN_CLOSED   =  9 # b <= a or b >  c
    NOT_IN_RANGE_CLOSED_OPEN   = 10 # b <  a or b >= c
    NOT_IN_RANGE_CLOSED_CLOSED = 11 # b <  a or b >  c
