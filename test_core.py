# -*- coding: utf-8 -*-
"""
Created on Fri Nov 6, 2020

@author: Alexander Neuhofer


"""
# import function, that should be tested
from core import foo


def test_foo():
    """ Simple function to explain usage of test file. 
	
	Each test function should check each function. """
    
    # assert = "behaupte, dass ..."
    assert foo(2) == 3