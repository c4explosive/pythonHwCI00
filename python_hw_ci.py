import os
import pytest
import mymodule

def hw_fx():
    print("Hello, World")
    return 0

def fx_math0(x, y):
    return x + -y

def multiply(x, y):
    return x * y

def test_fx_math0():
    assert fx_math0(5, 5) >= 0

def test_hw():
    assert hw_fx() == 0

def test_multiply():
    assert multiply(8, 12) > 89

def test_mymodule_divide():
    assert mymodule.divide(8, 3) >= -1