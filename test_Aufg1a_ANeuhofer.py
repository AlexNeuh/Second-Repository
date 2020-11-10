# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10, 2020
@author: Alexander Neuhofer
"""
from Aufg1a_ANeuhofer import is_prime


def test_isPrime():
    """ isPrime should check:
    		if input is prime or not and
		if input is positive or not. 	"""
    
    # assert = "behaupte, dass ..."
    assert is_prime(3) == print("Die Zahl 3 ist wirklich eine Primzahl!")
    assert is_prime(4) == print("Die Zahl 4 ist keine Primzahl!")
    assert is_prime(-2) == print("Zahl muss größer 1 sein!")
