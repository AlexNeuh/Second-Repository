# -*- coding: utf-8 -*-
"""
Created on Fri Nov 6, 2020

@author: Alexander Neuhofer


"""
import foo from core


def test_foo():
    """ Simple function to explain usage of test file. 
	- Each function should be checked with a test! """
    
    # assert = "behaupte, dass ..."
    assert foo(2) == 3
